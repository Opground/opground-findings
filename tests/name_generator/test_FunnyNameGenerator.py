import json
import re

import pytest
from opground.name_generator.FunnyNameGenerator import FunnyNameGenerator, NameCategory


@pytest.fixture
def funny_name_generator():
    return FunnyNameGenerator()


# using pytest with requests-mock https://requests-mock.readthedocs.io/en/latest/pytest.html
def test_name_category_generator(funny_name_generator, requests_mock):
    response_json = {
        "success": {"total": "null", "start": 0, "limit": 3},
        "contents": {
            "category": "elf",
            "variation": "null",
            "names": [
                "Raymond Trarie",
                "Maescia Gilbanise",
                "Bill Ianneiros",
            ],
        },
        "copyright": "https://fungenerators.com/",
    }
    requests_mock.get(funny_name_generator._base_endpoint, text=json.dumps(response_json))
    assert [
        "Raymond Trarie",
        "Maescia Gilbanise",
        "Bill Ianneiros",
    ] == funny_name_generator.generate(NameCategory.Elf)


def test_name_category_generator_mock_regex(funny_name_generator, requests_mock):
    response_json = {
        "success": {"total": "null", "start": 0, "limit": 3},
        "contents": {
            "category": "elf",
            "variation": "null",
            "names": [
                "Raymond Trarie",
                "Maescia Gilbanise",
                "Bill Ianneiros",
            ],
        },
        "copyright": "https://fungenerators.com/",
    }
    url_regex = re.compile("https://api.fungenerators.com/")
    requests_mock.get(url_regex, text=json.dumps(response_json))
    assert [
        "Raymond Trarie",
        "Maescia Gilbanise",
        "Bill Ianneiros",
    ] == funny_name_generator.generate(NameCategory.Elf)
