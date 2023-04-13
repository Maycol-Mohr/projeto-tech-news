import requests
from parsel import Selector
import time


# Requisito 1
def fetch(url: str, wait: int = 3) -> str:
    HEADERS = {"user-agent": 'Fake user-agent'}

    try:
        response = requests.get(url, timeout=wait, headers=HEADERS)
        time.sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content: str) -> str:
    # selector = Selector(string_content_html)
    # return selector.css(".entry-title a::attr(href)").getall()
    try:
        selector = Selector(html_content)
    except (requests.HTTPError, requests.ReadTimeout):
        return []
    else:
        return selector.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
