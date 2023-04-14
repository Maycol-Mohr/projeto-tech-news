from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from tech_news.database import find_news


@pytest.fixture
def mock_de_readable():
    return [
        {
            "readable": [  # Grupos de notícias que tem 'reading_time' menor ou igual ao parâmetro
                {
                    "unfilled_time": 3,  # tempo disponível restante (não preenchido pelas notícias escolhidas)
                    "chosen_news": [  # Lista de notícias escolhidas
                        (
                            "Não deixe para depois: Python é a linguagem mais quente do momento",  # 'title' da notícia
                            4,  # 'reading_time' da notícia
                        ),
                        (
                            "Selenium, BeautifulSoup ou Parsel? Entenda as diferenças",
                            3,
                        ),
                    ],
                },
                {
                    "unfilled_time": 0,
                    "chosen_news": [
                        (
                            "Pytest + Faker: a combinação poderosa dos testes!",
                            10,
                        )
                    ],
                },
            ],
        }
    ]


@pytest.fixture
def mock_de_unreadable():
    return [
        {
            "unreadable": [  # Lista de notícias que tem 'reading_time' maior que o parâmetro
                ("FastAPI e Flask: frameworks para APIs em Python", 15),
                ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
            ],
        }
    ]


@pytest.fixture
def mock_de_zero_time():
    return [
        {
            "unfilled_time": [  # Lista de notícias que tem 'reading_time' zero
                ("FastAPI e Flask: frameworks para APIs em Python", 0),
                ("A biblioteca Pandas e o sucesso da linguagem Python", 0),
            ],
        }
    ]


def test_reading_plan_group_news():
    encontrar_noticia = find_news()

    reading_time = ReadingPlanService(encontrar_noticia)

    reading_time.group_news_for_available_time(50)

    unreadable_time = ReadingPlanService(encontrar_noticia)

    unreadable_time.group_news_for_available_time(10)

    zero_time = ReadingPlanService(encontrar_noticia)

    zero_time.group_news_for_available_time(0)

    assert mock_de_readable == reading_time

    assert mock_de_unreadable == unreadable_time

    assert mock_de_zero_time == zero_time("Valor 'available_time' deve ser maior que zero")
