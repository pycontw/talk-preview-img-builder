"""
ImgBuilder Class
"""
import os
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from loguru import logger
from model import Material, Speaker
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
    speaker_right_pos: int
    speaker_upper_pos: int  # Will be updated depending on height of the content bottom
    speaker_margin: int = 10
    font: str = "PingFang.ttc"
    bold_font: str = "PingFang.ttc"
    text_color: str = "#000000"
    hightlight_text_color: str = "#ffffff"
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
        font = ImageFont.truetype(self.bold_font, size=28)
        # TODO: Update to wrap texts contained hybrid english and chinese
        if re.findall(r"[\u4e00-\u9fff]+", title):  # Detect if title contains Chinese
            # Chinesse title
            content = "\n".join(textwrap.wrap(title, width=20))
        else:
            # Default is english title
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

    def __fill_in_abstract(self, img: Image.Image, abstract: str):
        """
        Fill in the abstract of tha talk
        """
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font, size=18)
        lines = []
        abstract.replace("\r", "")
        # TODO: Update to wrap texts contained hybrid english and chinese
        if re.findall(
            r"[\u4e00-\u9fff]+", abstract
        ):  # Detect if abstract contains Chinese
            for line in abstract.split("\n"):
                lines += textwrap.wrap(line, width=30)
            display_text = "\n".join(lines)
        else:
            # Default is english abstract
            for line in abstract.split("\n"):
                lines += textwrap.wrap(line, width=60)
            display_text = "\n".join(lines)

        width, height = draw.multiline_textsize(display_text, font=font)
        pos_x, pos_y = (
            self.content_upper_left_pos[0] + (self.content_size[0] - width) / 2,
            self.content_upper_left_pos[1],
        )
        draw.multiline_text(
            (pos_x, pos_y),
            display_text,
            font=font,
            align="left",
            fill=self.text_color,
        )
        self.speaker_upper_pos = pos_y + height + self.speaker_margin

    def __fill_in_speaker(self, img: Image.Image, speakers: List[Speaker]):
        """
        Fill in the speaker of the talk
        """
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font, size=20)
        name_list = "、".join([speaker.name for speaker in speakers])
        display_text = f"— {name_list}"
        width, _ = draw.textsize(display_text, font=font)
        pos_x, pos_y = (
            self.speaker_right_pos - width - self.speaker_margin,
            self.speaker_upper_pos,
        )
        draw.text(
            (pos_x, pos_y),
            display_text,
            font=font,
            align="right",
            fill=self.text_color,
        )

    def __fill_in_footer(
        self, img: Image.Image, category: str, python_level: str, language: str
    ):
        """
        Fill in the category, python level, language of the talk
        """
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font, size=15)
        category_to_text = {
            "APPL": "應用",
            "PRAC": "最佳實踐與慣例",
            "COM": "社群",
            "DB": "資料庫",
            "DATA": "資料分析",
            "EDU": "教育",
            "EMBED": "嵌入式系統",
            "FIN": "金融科技",
            "IOT": "物聯網",
            "GAME": "遊戲",
            "GRAPH": "圖像處理",
            "ML": "機器學習",
            "NLP": "自然語言處理",
            "CORE": "Python 核心",
            "TOOL": "專案建置工具",
            "SCI": "科學",
            "SEC": "資訊安全",
            "ADMIN": "系統管理",
            "TEST": "測試",
            "WEB": "網站框架",
            "OTHER": "其他",
        }
        language_to_text = {
            "ENEN": "英文演講",
            "ZHEN": "中文演講/英文投影片",
            "ZHZH": "中文演講/中文投影片",
            "TAI": "臺灣閩南語",
        }
        python_level_to_text = {
            "EXPERIENCED": "●●●",
            "INTERMEDIATE": "●●○",
            "NOVICE": "●○○",
        }
        display_text = "    .    ".join(
            [
                category_to_text[category],
                f"語言：{language_to_text[language]}",
                f"Python 難易度：{python_level_to_text[python_level]}",
            ]
        )

        draw.text(
            self.footer_upper_left_pos,
            display_text,
            font=font,
            align="center",
            fill=self.hightlight_text_color,
        )

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
            self.__fill_in_abstract(output_image, talk.abstract)
            self.__fill_in_speaker(output_image, talk.speakers)
            self.__fill_in_footer(
                output_image,
                category=talk.category,
                python_level=talk.python_level,
                language=talk.language,
            )
            output_image.save(
                (
                    self.output_path
                    / (talk.title.replace(" ", "_").replace("/", "_") + ".png")
                ).resolve(),
                quality=95,
                subsampling=0,
            )
