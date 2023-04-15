from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_readable1():
    return {
        "readable": [
            {"chosen_news": [("A terra é redonda.", 1)], "unfilled_time": 3},
            {"chosen_news": [("O ceu é azul.", 3)], "unfilled_time": 1},
            {
                "chosen_news": [("O flamengo é campeao.", 4)],
                "unfilled_time": 0,
            },
        ],
        "unreadable": [("A lua é branca.", 5)],
    }


@pytest.fixture
def mock_readable2():
    return {
        "readable": [
            {"chosen_news": [("A terra é redonda.", 1)], "unfilled_time": 2},
            {"chosen_news": [("O ceu é azul.", 3)], "unfilled_time": 0},
        ],
        "unreadable": [("O flamengo é campeao.", 4), ("A lua é branca.", 5)],
    }


@pytest.fixture
def mock_news():
    return [
        {"title": "A terra é redonda.", "reading_time": 1},
        {"title": "O ceu é azul.", "reading_time": 3},
        {"title": "O flamengo é campeao.", "reading_time": 4},
        {"title": "A lua é branca.", "reading_time": 5},
    ]


def test_reading_plan_group_news(mock_readable1, mock_readable2, mock_news):
    with patch("tech_news.analyzer.reading_plan.find_news", lambda: mock_news):
        reading_time = ReadingPlanService()

        assert mock_readable1 == reading_time.group_news_for_available_time(4)

        assert mock_readable2 == reading_time.group_news_for_available_time(3)

        with pytest.raises(ValueError):
            reading_time.group_news_for_available_time(-10)
