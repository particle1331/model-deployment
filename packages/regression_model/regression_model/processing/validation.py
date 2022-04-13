import numpy as np
import pandas as pd
from pydantic import ValidationError

from regression_model.config.core import config
from regression_model.processing.schemas import MultipleHouseDataInputs


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""

    # Columns in train data with missing values
    train_vars_with_na = (
        config.model_config.categorical_vars_with_na_frequent
        + config.model_config.categorical_vars_with_na_missing
        + config.model_config.numerical_vars_with_na
    )

    # At least one example in column var is missing
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if var not in train_vars_with_na and input_data[var].isnull().sum() > 0
    ]

    # Drop rows
    return input_data.dropna(axis=0, subset=new_vars_with_na)


def validate_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for unprocessable values."""

    selected_features = config.model_config.features
    validated_data = input_data.rename(columns=config.model_config.variables_to_rename)
    validated_data = validated_data[selected_features].copy()
    validated_data = drop_na_inputs(input_data=validated_data)
    validated_data["MSSubClass"] = validated_data["MSSubClass"].astype("O")
    errors = None

    try:
        # Replace numpy nans so that pydantic can validate
        MultipleHouseDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as e:
        errors = e.json()

    return validated_data, errors
