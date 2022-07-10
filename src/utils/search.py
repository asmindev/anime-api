import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from urllib.parse import urlparse
from typing import List, Text, Dict

load_dotenv()
host = os.getenv("OTAKUDESU")


class Search:
    def __init__(self) -> None:
        self._query = None
        pass

    def __repr__(self) -> Text:
        return f"<Search anime from {host}>"

    def __get_content(self) -> BeautifulSoup:
        url = f"{host}/find/?keyword={self._query}"
        r = requests.get(url)
        return BeautifulSoup(r.text, "html.parser")

    def __parse_content(self) -> List[Dict]:
        results = []
        content = self.__get_content()
        slug = None
        row = content.find("div", {"class": "col-md-8"})
        articles = row.find_all("article", {"class": "article"})
        for article in articles:
            title = article.find("h4", {"class": "article-title"})
            if title:
                title = title.find("a").text
            thumbnail = article.find("div", {"class": "article-img"})
            url = thumbnail.find("a")
            if url.get("href"):
                slug = urlparse(url.get("href")).path.split("/")[-2]
            if thumbnail:
                thumbnail_alt = thumbnail.find("img").get("alt")
                thumbnail = thumbnail.find("img").get("src")

            results.append(
                dict(
                    title=title,
                    slug=slug,
                    url=url.get("href"),
                    thumbnail=dict(image=thumbnail, alt=thumbnail_alt),
                )
            )
        return results

    def get(self, query: Text) -> List[Dict]:
        self._query = query
        return self.__parse_content()


# t = Search()
# print(t)
# print(t.get("naruto"))
