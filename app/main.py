"""Main module for running app"""
from enum import Enum

import typer
from config import Settings
from img_builder import TalkPreviewImgBuilder
from loguru import logger
from model import Material


def build_talk_preview_img():
    """Build preview images from material"""
    settings = Settings()
    logger.debug("Loading configuration {}", Settings())
    material = Material(
        talk_resource_path=settings.TALKS_PATH,
        pycon_logo_path=settings.PYCON_LOGO_PATH,
        talk_category_icon_path=settings.TALK_CATEGORY_ICON_PATH,
        python_level_empty_icon_path=settings.PYTHON_LEVEL_EMPTY,
        python_level_filled_icon_path=settings.PYTHON_LEVEL_FILLED,
        quote_img_path=settings.QUOTE_IMG_PATH,
    )
    material.load()
    preview_img_builder = TalkPreviewImgBuilder(
        material=material,
        background_color=settings.PREVIEW_BACKGROUND_COLOR,
        content_background_color=settings.PREVIEW_CONTENT_BACKGROUND_COLOR,
    )
    preview_img_builder.execute()


class TaskName(str, Enum):
    """All avaliable tasks"""

    build_talk_preview_img = "build_talk_preview_img"  # pylint: disable=invalid-name


def main(task_name: TaskName):
    """Main function for running app"""
    task_name_to_func = {"build_talk_preview_img": build_talk_preview_img}
    task_name_to_func[task_name]()


if __name__ == "__main__":
    typer.run(main)
