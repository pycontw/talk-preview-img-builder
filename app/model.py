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
    background_img_path: Path

    def __post_init__(self):
        self.talk_list = []
        self.background_img = None

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

        if not self.background_img_path.exists():
            raise FileNotFoundError(f"{self.background_img_path} not found")
        logger.info("Loading {}", self.background_img_path.resolve())
        self.background_img = Image.open(self.background_img_path.resolve())
