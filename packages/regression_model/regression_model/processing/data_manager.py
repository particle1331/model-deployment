import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from regression_model import __version__ as _version
from regression_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def clean_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Clean data to avoid syntax errors later."""

    input_data.rename(columns=config.model_config.variables_to_rename, inplace=True)
    input_data["MSSubClass"] = input_data["MSSubClass"].astype("O")
    return input_data


def load_dataset(*, file_name: str) -> pd.DataFrame:
    """Load and clean dataset."""

    dataframe = pd.read_csv(DATASET_DIR / file_name)
    dataframe = clean_inputs(input_data=dataframe)
    return dataframe


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    """Persist the pipeline.
    Saves the versioned model, and overwrites any previous saved models.
    This ensures that when the package is published, there is only one
    trained model that can be called, and we know exactly how it was built."""

    # Prepare versioned save file name
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines()
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines() -> None:
    """Remove old model pipelines.
    This is to ensure there is a simple one-to-one mapping between
    the package version and the model version to be imported and
    used by other applications."""

    do_not_delete = ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()  # Delete
