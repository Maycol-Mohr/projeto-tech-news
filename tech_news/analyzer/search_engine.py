from tech_news.database import search_news
from datetime import datetime


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
    empty_list = []

    try:
        iso_date = '%Y-%m-%d'
        db_date = '%d/%m/%Y'

        correct_date = datetime.strptime(date, iso_date).strftime(db_date)
        # data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        query_correct_date = {'timestamp': correct_date}

        news_list = search_news(query_correct_date)

        for new_date in news_list:
            empty_list.append((new_date['title'], new_date['url']))
        return empty_list

    except ValueError:
        raise ValueError(
            'Data inválida'
        )

    finally:
        'OK'


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
