import numpy as np
from pydantic import ValidationError
from sklearn.model_selection import train_test_split

from regression_model.config.core import config
from regression_model.pipeline import price_pipe
from regression_model.processing.data_manager import load_dataset, save_pipeline
from regression_model.processing.validation import validate_inputs


def run_training() -> None:
    """Train the model."""

    # Read and validate training data
    data = load_dataset(file_name=config.app_config.training_data_file)
    X = data[config.model_config.features]
    y = data[config.model_config.target]
    X, errors = validate_inputs(input_data=X)
    if errors:
        raise ValidationError

    # Divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )
    y_train = np.log(y_train)  # <-- ⚠ Invert before serving preds

    # Fit model
    price_pipe.fit(X_train, y_train)

    # Persist trained model
    save_pipeline(pipeline_to_persist=price_pipe)


if __name__ == "__main__":
    run_training()
