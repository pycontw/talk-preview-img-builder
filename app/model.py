"""
Datamodel that be used in this app
"""
import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from loguru import logger
from PIL import Image


@dataclass
class ImageFile:
    """
    Image components used for building preview image.
    """

    path: Path
    image: Image.Image
    name: Optional[str]


@dataclass
class Speaker:
    """
    Speaker model referred in talk info
    """

    thumbnail_url: str
    name: str
    github_profile_url: Optional[str] = ""
    twitter_profile_url: Optional[str] = ""
    facebook_profile_url: Optional[str] = ""
    bio: Optional[str] = ""


@dataclass
class Talk:
    """
    Talk model
    """

    title: str
    category: str
    abstract: str
    python_level: str  # EXPERIENCED, INTERMEDIATE
    speakers: List[Speaker]
    language: str


@dataclass
class Material:  # pylint: disable=too-many-instance-attributes
    """
    Materials that will be used in building the image.
    """

    talk_resource_path: Path
    pycon_logo_path: Optional[Path] = None
    talk_category_icon_path: Optional[Path] = None
    python_level_empty_icon_path: Optional[Path] = None
    python_level_filled_icon_path: Optional[Path] = None
    quote_img_path: Optional[Path] = None

    def __post_init__(self):
        self.talk_list = []
        self.loaded_images = []
        self.pycon_logog = None
        self.talk_category_icon = None
        self.python_level_empty_icon = None
        self.python_level_filled_icon = None
        self.quote_img = None

    def load(self):
        """
        Load all the images and talks used for building the image.
        """
        with open(self.talk_resource_path.resolve()) as fin:
            for talk in json.load(fin):
                self.talk_list.append(
                    Talk(
                        title=talk["title"],
                        category=talk["category"],
                        abstract=talk["abstract"],
                        python_level=talk["python_level"],
                        speakers=[Speaker(**speaker) for speaker in talk["speakers"]],
                        language=talk["language"],
                    )
                )

        for path, name in [
            (self.pycon_logo_path, "pycon_logo"),
            (self.talk_category_icon_path, "talk_category_icon"),
            (self.python_level_empty_icon_path, "python_level_empty_icon"),
            (self.python_level_filled_icon_path, "python_level_filled_icon"),
            (self.quote_img_path, "quote_img"),
        ]:
            if path and not path.exists():
                raise FileNotFoundError(f"{path} not found")
            if not path:
                continue
            logger.info("Loading {}", path.resolve())
            img = ImageFile(path, Image.open(path.resolve()), path.stem)
            self.loaded_images.append(img)
            setattr(self, name, img)
