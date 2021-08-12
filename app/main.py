"""Main module for running app"""
from enum import Enum

import typer
from config import ImgBuilderSettings, PPTBuilderSettings
from img_builder import TalkPreviewImgBuilder
from loguru import logger
from model import Material
from ppt_builder import TalkPreviewPPTBuilder


def build_talk_preview(output_format: str):
    """Build preview images from material"""
    if output_format == OutputFormat.ppt.value:
        # TODO: Implement builder adapter
        settings = PPTBuilderSettings()
        logger.debug("Loading configuration {}", settings)
        material = Material(
            talk_resource_path=settings.SPEECHES_PATH,
            background_img_path=settings.BACKGROUND_IMG_PATH,
        )
        material.load()
        preview_ppt_builder = TalkPreviewPPTBuilder(
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
            text_color=settings.PREVIEW_TEXT_COLOR,
            hightlight_text_color=settings.PREVIEW_HIGHTLIGHT_TEXT_COLOR,
            font=settings.PREVIEW_TEXT_FONT,
            bold_font=settings.PREVIEW_TEXT_BOLD_FONT,
        )
        preview_ppt_builder.execute()
    elif output_format == OutputFormat.png.value:
        # TODO: Implement builder adapter
        settings = ImgBuilderSettings()
        logger.debug("Loading configuration {}", settings)
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
            text_color=settings.PREVIEW_TEXT_COLOR,
            hightlight_text_color=settings.PREVIEW_HIGHTLIGHT_TEXT_COLOR,
            font=settings.PREVIEW_TEXT_FONT,
            bold_font=settings.PREVIEW_TEXT_BOLD_FONT,
        )
        preview_img_builder.execute()
    else:
        logger.error("Unknown output format {}", output_format)


class TaskName(str, Enum):
    """All avaliable tasks"""

    build_talk_preview = "build_talk_preview"  # pylint: disable=invalid-name


class OutputFormat(str, Enum):
    """All avaliable output formats"""

    ppt = "ppt"  # pylint: disable=invalid-name
    png = "png"  # pylint: disable=invalid-name


def main(
    task_name: TaskName,
    output: OutputFormat = typer.Option(
        OutputFormat.ppt, help="Output format like ppt or png"
    ),
):
    """Main function for running app"""
    task_name_to_func = {"build_talk_preview": build_talk_preview}
    task_name_to_func[task_name](output_format=output.value)


if __name__ == "__main__":
    typer.run(main)
