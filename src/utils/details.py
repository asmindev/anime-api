import os
import requests
from typing import Any, Text, Dict
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()


class Details:
    def __init__(self):
        self.url = os.getenv("OTAKUDESU")
        self.anime_slug = None

    def __repr__(self):
        return f"< Get Details anime from {self.url}>"

    def __get_content(self) -> BeautifulSoup:
        url = f"{self.url}/movie/{self.anime_slug}"
        r = requests.get(url)
        return BeautifulSoup(r.text, "html.parser")

    def __parse_content(self) -> Dict[Any, Any]:
        thumbnails = {}
        paragraphs = None
        published = None
        info = {}
        content = self.__get_content()
        article = content.find("article", {"class": "article"})
        title = article.find("h1", {"class": "article-title3"}).text
        thumbnail = article.find("div", {"class": "article-main-img"})
        if thumbnail:
            thumbnail_img = thumbnail.find("img").get("src")
            thumbnail_alt = thumbnail.find("img").get("alt")
            thumbnails = dict(image=thumbnail_img, alt=thumbnail_alt)
        article_body = article.find("div", {"class": "article-body"})
        if article_body:
            published = article_body.find("time", {"itemprop": "datePublished"})
            if published:
                published = published.text
            paragraphs = article_body.find_all("p")
            paragraphs = [p.text for p in paragraphs]
            paragraphs = "".join(paragraphs)
            info.update({"published": published})
            info.update({"paragraphs": paragraphs})
            div = article_body.find_all("div")
            div = [d for d in div if d.find("i")]
            for i in div:
                i = i.text.split(":")
                if i[0].endswith(" "):
                    i[0] = i[0].strip()  # remove space
                if " " in i[0]:
                    print(i[0])
                    i[0] = i[0].replace(" ", "_")
                if i[1].startswith(" "):
                    i[1] = i[1].strip()
                info.update({i[0].lower(): i[1]})
            info["genre"] = info["genre"].strip().split(", ")

        return dict(
            title=title,
            info=info,
            thumbnails=thumbnails,
        )

    def get(self, slug: Text) -> Dict[Any, Any]:
        self.anime_slug = slug
        return self.__parse_content()


if __name__ == "__main__":
    t = Details()
    print(t.get("spy-x-family-dk1wetfdqu"))
