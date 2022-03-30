from regression_model.config.core import PACKAGE_ROOT

VERSION_PATH = PACKAGE_ROOT / "VERSION"
name = "regression_model"

with open(VERSION_PATH, "r") as version_file:
    __version__ = version_file.read().strip()
