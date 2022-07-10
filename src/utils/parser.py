from typing import Text
from bs4 import BeautifulSoup
import requests


def parse_html(url: Text) -> BeautifulSoup:
    """
    Parses the html of a given url and returns the content.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup
