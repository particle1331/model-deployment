import typing as t

import numpy as np
import pandas as pd

from regression_model import __version__ as _version
from regression_model.config.core import config
from regression_model.processing.data_manager import load_pipeline
from regression_model.processing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    predictions, errors = None, None

    try:
        validated_data = validate_inputs(input_data=data)
        X = validated_data[config.model_config.features]
        predictions = [np.exp(y) for y in _price_pipe.predict(X=X)]

    except Exception as e:
        errors = e

    results = {
        "predictions": predictions,
        "version": _version,
        "errors": errors,
    }

    return results
