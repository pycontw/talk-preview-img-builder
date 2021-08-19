"""App configuration"""
from pathlib import Path

from pydantic import BaseSettings


class ImgBuilderSettings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Settings for the img builder"""

    BACKGROUND_IMG_PATH: Path = (
        Path(__file__).parent.parent / "material" / "img" / "background.png"
    )

    SPEECHES_PATH: Path = Path(__file__).parent.parent / "material" / "speeches.json"

    # Unit: px
    PREVIEW_IMG_WIDTH: int = 700
    PREVIEW_IMG_HEIGHT: int = 700
    PREVIEW_IMG_TITLE_UPPER_LEFT_X: int = 110
    PREVIEW_IMG_TITLE_UPPER_LEFT_Y: int = 110
    PREVIEW_IMG_CONTENT_UPPER_LEFT_X: int = 85
    PREVIEW_IMG_CONTENT_UPPER_LEFT_Y: int = 200
    PREVIEW_IMG_FOOTER_UPPER_LEFT_X: int = 100
    PREVIEW_IMG_FOOTER_UPPER_LEFT_Y: int = 650
    PREVIEW_IMG_SPEAKER_UPPER_RIGHT_Y: int = 570
    PREVIEW_IMG_SPEAKER_UPPER_RIGHT_X: int = 600
    TITLE_HEIGHT: int = 70
    CONTENT_HEIGHT: int = 90
    PREVIEW_TEXT_COLOR: str = "#080A42"
    PREVIEW_HIGHTLIGHT_TEXT_COLOR: str = "#EBCC73"
    PREVIEW_TEXT_FONT: str = "PingFang.ttc"
    PREVIEW_TEXT_BOLD_FONT: str = "PingFang.ttc"

    class Config:  # pylint: disable=too-few-public-methods
        """Settings Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"


class PPTBuilderSettings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Settings for the ppt builder"""

    BACKGROUND_IMG_PATH: Path = (
        Path(__file__).parent.parent / "material" / "img" / "background.png"
    )

    SPEECHES_PATH: Path = Path(__file__).parent.parent / "material" / "speeches.json"

    # Unit: cm
    PREVIEW_IMG_WIDTH: float = 14
    PREVIEW_IMG_HEIGHT: float = 14
    PREVIEW_IMG_TITLE_UPPER_LEFT_X: float = 0.95
    PREVIEW_IMG_TITLE_UPPER_LEFT_Y: float = 1.04
    PREVIEW_IMG_CONTENT_UPPER_LEFT_X: float = 1.38
    PREVIEW_IMG_CONTENT_UPPER_LEFT_Y: float = 3.8
    PREVIEW_IMG_FOOTER_UPPER_LEFT_X: float = 1.6
    PREVIEW_IMG_FOOTER_UPPER_LEFT_Y: float = 12.2
    PREVIEW_IMG_SPEAKER_UPPER_RIGHT_X: float = 13.5
    PREVIEW_IMG_SPEAKER_UPPER_RIGHT_Y: float = 10
    TITLE_HEIGHT: float = 1.84
    CONTENT_HEIGHT: float = 7.5
    PREVIEW_TEXT_COLOR: str = "#080A42"
    PREVIEW_HIGHTLIGHT_TEXT_COLOR: str = "#EBCC73"
    PREVIEW_TEXT_FONT: str = "Taipei Sans TC Beta"
    PREVIEW_TEXT_BOLD_FONT: str = "Taipei Sans TC Beta"

    class Config:  # pylint: disable=too-few-public-methods
        """Settings Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"
