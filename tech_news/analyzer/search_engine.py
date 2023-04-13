from tech_news.database import search_news


# Requisito 7
def search_by_title(title) -> 'list[dict]':
    search_title = {'title': {"$regex": title, '$options': 'i'}}
    new_title_list = search_news(search_title)
    empty_list = []

    for new_title in new_title_list:
        empty_list.append((new_title['title'], new_title['url']))
    return empty_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
