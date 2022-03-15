from pathlib import Path
from typing import Dict, List, Sequence

from pydantic import BaseModel
from strictyaml import YAML, load

import regression_model

# Project Directories
PACKAGE_ROOT = Path(regression_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class AppConfig(BaseModel):
    """
    Application-level config.
    """

    package_name: str
    training_data_file: str
    test_data_file: str
    pipeline_save_file: str


class ModelConfig(BaseModel):
    """
    All configuration relevant to model training and feature engineering.
    """

    target: str
    variables_to_rename: Dict
    features: List[str]
    test_size: float
    random_state: int
    alpha: float
    categorical_vars_with_na_frequent: List[str]
    categorical_vars_with_na_missing: List[str]
    numerical_vars_with_na: List[str]
    temporal_vars: List[str]
    ref_var: str
    numericals_log_vars: Sequence[str]
    binarize_vars: Sequence[str]
    qual_vars: List[str]
    exposure_vars: List[str]
    finish_vars: List[str]
    garage_vars: List[str]
    categorical_vars: Sequence[str]
    qual_mappings: Dict[str, int]
    exposure_mappings: Dict[str, int]
    garage_mappings: Dict[str, int]
    finish_mappings: Dict[str, int]


class Config(BaseModel):
    """Master config object."""

    app_config: AppConfig
    model_config: ModelConfig


def validate_config_file_path(cfg_path: Path) -> Path:
    """Locate the configuration file."""

    if not cfg_path.is_file():
        raise OSError(f"Config not found at {cfg_path!r}")

    return cfg_path


def parse_config_from_yaml(cfg_path: Path) -> YAML:
    """Parse YAML containing the package configuration."""

    cfg_path = validate_config_file_path(cfg_path)
    with open(cfg_path, "r") as conf_file:
        parsed_config = load(conf_file.read())

    return parsed_config


def create_and_validate_config(parsed_config: YAML) -> Config:
    """Run validation on config values."""

    return Config(
        app_config=AppConfig(**parsed_config.data),
        model_config=ModelConfig(**parsed_config.data),
    )


_parsed_config = parse_config_from_yaml(CONFIG_FILE_PATH)
config = create_and_validate_config(_parsed_config)
