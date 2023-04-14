import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories


def analyzer_menu():
    opcao = input(
        'Selecione uma das opções a seguir:\n'
        ' 0 - Popular o banco com notícias;\n'
        ' 1 - Buscar notícias por título;\n'
        ' 2 - Buscar notícias por data;\n'
        ' 3 - Buscar notícias por categoria;\n'
        ' 4 - Listar top 5 categorias;\n'
        ' 5 - Sair.'
    )

    match opcao:
        case '0':
            amount = input('Digite quantas notícias serão buscadas:')
            get_tech_news(int(amount))
        case '1':
            title = input('Digite o título:')
            search_by_title(title)
        case '2':
            date = input('Digite a data no formato aaaa-mm-dd:')
            search_by_date(date)
        case '3':
            category = input('Digite a categoria:')
            search_by_category(category)
        case '4':
            top_5_categories()
        case '5':
            print('Encerrando script')
        case _:
            sys.stderr.write('Opção inválida\n')
        # sys.stderr.write("Mensagem de erro aqui\n")
