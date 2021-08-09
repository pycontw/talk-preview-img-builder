"""App configuration"""
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Settings for the app"""

    TALK_CATEGORY_ICON_PATH: Path = (
        Path(__file__).parent.parent / "material" / "img" / "category_icon.png"
    )
    PYCON_LOGO_PATH: Path = (
        Path(__file__).parent.parent / "material" / "img" / "logo.png"
    )
    PYTHON_LEVEL_EMPTY: Path = (
        Path(__file__).parent.parent / "material" / "img" / "python_level_empty.png"
    )
    PYTHON_LEVEL_FILLED: Path = (
        Path(__file__).parent.parent / "material" / "img" / "python_level_filled.png"
    )
    QUOTE_IMG_PATH: Path = (
        Path(__file__).parent.parent / "material" / "img" / "quote.png"
    )
    TALKS_PATH: Path = Path(__file__).parent.parent / "material" / "talks.json"

    PREVIEW_BACKGROUND_COLOR: str = "#FCE1D4"
    PREVIEW_TEXT_COLOR: str = "#885E5C"
    PREVIEW_CONTENT_BACKGROUND_COLOR: str = "#FEF0EA"

    class Config:  # pylint: disable=too-few-public-methods
        """Settings Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"
