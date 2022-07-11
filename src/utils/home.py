import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from typing import List, Text, Dict

load_dotenv()
host = os.getenv("OTAKUDESU")


class Home:
    def __init__(self) -> None:
        self.__page = None
        pass

    def __repr__(self) -> Text:
        return f"Home anime from {host}"

    def __get_content(self) -> BeautifulSoup:
        if self.__page:

            url = f"{host}/home/page/{self.__page}"
        else:
            url = f"{host}/home"
        r = requests.get(url)
        return BeautifulSoup(r.text, "html.parser")

    def __parse_content(self) -> List[Dict]:
        results = []
        content = self.__get_content()
        row = content.find("div", {"class": "col-md-8"})
        articles = row.find_all("article", {"class": "article"})
        for article in articles:
            title = article.find("h3", {"class": "article-title"})
            if title:
                title = title.find("a").text
            thumbnail = article.find("div", {"class": "article-img"})
            url = {}
            info = {}
            if thumbnail:
                article_info = thumbnail.find("li", {"class": "article-type"})
                if article_info:
                    info.update({"episode": article_info.text})
                url = thumbnail.find("a")
                thumbnail_alt = thumbnail.find("img").get("alt")
                thumbnail = thumbnail.find("img").get("src")
            published = article.find("span", {"itemprop": "datePublished"})
            info.update({"published": published.text})
            results.append(
                dict(
                    title=title,
                    url=url.get("href"),
                    info=info,
                    thumbnail=dict(image=thumbnail, alt=thumbnail_alt),
                )
            )
        return results

    def get(self, page=None) -> List[Dict]:
        if page and page.isdigit() and int(page) > 1:
            self.__page = page
        return self.__parse_content()


if __name__ == "__main__":
    t = Home()
    print(t)
    # print(t.get())
