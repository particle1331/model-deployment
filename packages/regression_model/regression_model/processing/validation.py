import pandas as pd

from regression_model.config.core import config
from regression_model.processing.schemas import HouseDataInputSchema


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
    input_data = input_data.rename(columns=config.model_config.variables_to_rename)
    input_data = input_data[selected_features].copy()
    input_data = drop_na_inputs(input_data=input_data)

    schema = HouseDataInputSchema.select_columns(selected_features)
    validated_data = schema.validate(input_data)
    return validated_data
