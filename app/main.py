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
        talk_resource_path=settings.SPEECHES_PATH,
        background_img_path=settings.BACKGROUND_IMG_PATH,
    )
    material.load()
    logger.debug("{} Loaded", material)
    preview_img_builder = TalkPreviewImgBuilder(
        material=material,
        size=(settings.PREVIEW_IMG_WIDTH, settings.PREVIEW_IMG_HEIGHT),
        title_upper_left_pos=(
            settings.PREVIEW_IMG_TITLE_UPPER_LEFT_X,
            settings.PREVIEW_IMG_TITLE_UPPER_LEFT_Y,
        ),
        content_upper_left_pos=(
            settings.PREVIEW_IMG_CONTENT_UPPER_LEFT_X,
            settings.PREVIEW_IMG_CONTENT_UPPER_LEFT_Y,
        ),
        footer_upper_left_pos=(
            settings.PREVIEW_IMG_FOOTER_UPPER_LEFT_X,
            settings.PREVIEW_IMG_FOOTER_UPPER_LEFT_Y,
        ),
        speaker_upper_pos=settings.PREVIEW_IMG_SPEAKER_UPPER_RIGHT_Y,
        speaker_right_pos=settings.PREVIEW_IMG_SPEAKER_UPPER_RIGHT_X,
        title_height=settings.TITLE_HEIGHT,
        content_height=settings.CONTENT_HEIGHT,
        footer_height=settings.FOOTER_HEIGHT,
        text_color=settings.PREVIEW_TEXT_COLOR,
        font=settings.PREVIEW_TEXT_FONT,
        bold_font=settings.PREVIEW_TEXT_BOLD_FONT,
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
