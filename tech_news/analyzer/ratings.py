from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    categories = []

    for category in find_news():
        categories.append(category['category'])

    counter = Counter(sorted(categories))
    sorted_monst_commom = counter.most_common(5)

    categories_sorted = []

    for category in sorted_monst_commom:
        categories_sorted.append(category[0])
    return categories_sorted
