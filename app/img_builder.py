"""
ImgBuilder Class
"""
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from model import Material
from PIL import Image


@dataclass
class TalkPreviewImgBuilder:  # pylint: disable=too-many-instance-attributes
    """
    ImgBuilder for building image by given materials
    """

    background_color: str
    content_background_color: str
    material: Material
    content_margin: int = 33
    size: Tuple[int, int] = (592, 592)
    file_name: str = "out.png"
    output_path: Path = Path(__file__).parent.parent / "export"

    def __locate_pycon_logo(self, img: Image.Image):
        """
        Locate the pycon logo
        """

    def __fill_in_title(self, img: Image.Image):
        """
        Draw the title
        """

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
        if not self.output_path.exists():
            os.mkdir(self.output_path.resolve())
        output_image = Image.new("RGB", self.size, self.background_color)
        self.__locate_pycon_logo(output_image)
        self.__fill_in_title(output_image)
        self.__fill_in_abstract(output_image)
        self.__fill_in_speaker(output_image)
        self.__fill_in_category(output_image)
        self.__fill_in_language(output_image)
        self.__fill_in_python_level(output_image)
        output_image.save(self.output_path.resolve() / self.file_name)
