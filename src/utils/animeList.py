from . import parser
from dotenv import load_dotenv
from urllib.parse import urlparse
import os

load_dotenv()


class AnimeList:
    def __init__(self):
        self.page = None
        self.url = os.getenv("OTAKUDESU", "https://otakudesu.to")

    def __get_ongoing(self):
        if self.page:
            url = self.url + "/anime-list/page/" + self.page
        else:
            url = self.url + "/anime-list"

        return parser.parse_html(url)

    def __parse_content(self):
        results = []
        content = self.__get_ongoing()
        cards = content.find_all("div", {"class": "col-md-3 col-sm-3"})
        for card in cards:
            field = dict(
                title=None,
                url=None,
                thumbnail=dict(image=None, alt=None),
                slug=None,
            )
            title = card.find("h4", {"class": "article-title"})
            field["title"] = title.text
            thumbnails = card.find("div", {"class": "article-img"})
            if thumbnails:
                img = thumbnails.find("img").get("src")
                alt = thumbnails.find("img").get("alt")
                field["thumbnail"]["image"] = img
                field["thumbnail"]["alt"] = alt
                url = card.find("a").get("href")
                slug = urlparse(url).path.split("/")[-2]
                field["url"] = url
                field["slug"] = slug
            results.append(field)
        return results

    def get(self, page=None):
        if page and page.isdigit() and int(page) > 1:
            self.page = page
        return self.__parse_content()


if __name__ == "__main__":
    t = AnimeList()
    t.get()
