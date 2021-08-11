"""
ImgBuilder Class
"""
import os
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from loguru import logger
from model import Material
from PIL import Image, ImageDraw, ImageFont


@dataclass
class TalkPreviewImgBuilder:  # pylint: disable=too-many-instance-attributes
    """
    ImgBuilder for building image by given materials
    """

    material: Material
    size: Tuple[int, int]
    title_upper_left_pos: Tuple[int, int]
    content_upper_left_pos: Tuple[int, int]
    footer_upper_left_pos: Tuple[int, int]
    title_height: int
    content_height: int
    footer_height: int
    text_color: str = "#000000"
    font: str = "PingFang.ttc"
    output_path: Path = Path(__file__).parent.parent / "export"

    def __post_init__(self):
        """
        Post initialization
        """
        self.content_size = (
            self.size[0] - self.content_upper_left_pos[0] * 2,
            self.content_height,
        )
        self.title_size: Tuple[int, int] = (
            self.size[0] - self.title_upper_left_pos[0] * 2,
            self.title_height,
        )

    def __fill_in_title(self, img: Image.Image, title: str):
        """
        Fill in the title
        """
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font, size=30)
        content = "\n".join(textwrap.wrap(title, width=35))
        width, height = draw.multiline_textsize(content, font=font)
        pos_x, pos_y = (
            self.title_upper_left_pos[0] + (self.title_size[0] - width) / 2,
            self.title_upper_left_pos[1] + (self.title_size[1] - height) / 2,
        )
        draw.multiline_text(
            (pos_x, pos_y),
            content,
            font=font,
            align="center",
            fill=self.text_color,
        )

    def __fill_in_abstract(self, img: Image.Image):
        """
        Fill in the abstract of tha talk
        """

    def __fill_in_speaker(self, img: Image.Image):
        """
        Fill in the speaker of the talk
        """

    def __fill_in_category(self, img: Image.Image):
        """
        Fill in the category of the talk
        """

    def __fill_in_language(self, img: Image.Image):
        """
        Fill in the language of the talk
        """

    def __fill_in_python_level(self, img: Image.Image):
        """
        Fill in the python level of the talk
        """

    def execute(self):
        """
        Execute the builder
        """
        if not self.material.background_img:
            return
        for talk in self.material.talk_list:
            logger.info("Building preview image for speech: {}...", talk.title)
            if not self.output_path.exists():
                os.mkdir(self.output_path.resolve())
            output_image = self.material.background_img.copy()
            self.__fill_in_title(output_image, talk.title)
            self.__fill_in_abstract(output_image)
            self.__fill_in_speaker(output_image)
            self.__fill_in_category(output_image)
            self.__fill_in_language(output_image)
            self.__fill_in_python_level(output_image)
            output_image.save(
                (self.output_path / (talk.title.replace(" ", "_") + ".png")).resolve(),
                quality=95,
                subsampling=0,
            )
