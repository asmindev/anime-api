import os

from bs4 import BeautifulSoup
from . import parser
from typing import Text, List, Dict
from dotenv import load_dotenv

load_dotenv()


class GetVideo:
    def __init__(self) -> None:

        self.__id = None
        self.__anime_slug = None
        self.url = os.getenv("OTAKUDESU", "")

    def __repr__(self) -> str:
        return "Get Video from {}".format(self.url)

    def __get_content(self) -> BeautifulSoup:
        # https://otakudesu.to/movie/naruto-shippuuden-movie-6-road-to-ninja-uqth9y3imq/?ep=1
        url = f"{self.url}/movie/{self.__anime_slug}/?ep={self.__id}"
        print(url)
        return parser.parse_html(url)

    def __parsing_content(self) -> Dict:
        content = self.__get_content()
        # print(content)
        video_url = content.find("iframe", {"data-src": True}).get("src", "")
        title = content.find("h1", {"class": "article-title2"}).text.strip()
        return dict(title=title, video_url=video_url)

    def get(self, id: int, anime_slug: Text) -> Dict:
        self.__id = id
        self.__anime_slug = anime_slug
        return self.__parsing_content()
