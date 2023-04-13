import requests
from parsel import Selector
import time

from tech_news.database import create_news


# Requisito 1
def fetch(url: str, wait: int = 3) -> str:
    HEADERS = {"user-agent": "Fake user-agent"}

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
    # selector = Selector(html_content)
    # next_page = selector.css(".next::attr(href)").get()
    # return next_page
    try:
        selector = Selector(html_content)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return selector.css(".next::attr(href)").get()


# Requisito 4
def scrape_news(html_content: str) -> str:
    selector = Selector(html_content)

    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").re_first(r"\d*")
        ),
        "summary": ''.join(selector.css(
            ".entry-content > p:nth-of-type(1) *::text").getall()).strip(),
        "category": selector.css(".label::text").get(),
    }


# Requisito 5
def get_tech_news(amount) -> 'list[dict]':
    base_url = fetch('https://blog.betrybe.com/')
    new_list = []

    while len(new_list) < amount:
        new_list = new_list + scrape_updates(base_url)

        if len(new_list) < amount:
            base_url = fetch(scrape_next_page_link(base_url))

    new_dict_list = [
        scrape_news(fetch(url))
        for url in new_list[:amount]
    ]

    create_news(new_dict_list)

    return new_dict_list
