from enum import Enum, auto

import requests


class NameCategory(Enum):
    Elf = auto()
    SuperHero = auto()
    Alien = auto()
    Dragon = auto()

    def __str__(self) -> str:
        dict_str = {
            self.Elf: "elf",
            self.SuperHero: "super-hero",
            self.Alien: "alien",
            self.Dragon: "dragon",
        }
        return dict_str[self]


class FunnyNameGenerator:
    """Funny name generator class usign https://fungenerators.com/api/namegen/#authentication endpoint."""

    def __init__(self) -> None:
        self._base_endpoint = "https://api.fungenerators.com/name/generate"

    def generate(self, category: NameCategory, max_number=10):
        """Generate funny names using the 'generator' endpoint.
        An example json response:
        {
            "success": {
            "total": null,
            "start": 0,
            "limit": 3
            },
            "contents": {
                "category": "car",
                "variation": null,
                "names": [
                "Mythic",
                "Intro",
                "Orbit",
                ]
            },
            "copyright": "https://fungenerators.com/"
        }

        Args:
            category (NameCategory): name category to generate names of.
            max_number (int, optional): maximum number of names to generate. Defaults to 10.
        """
        endpoint = f"{self._base_endpoint}?category={str(category)}&limit={max_number}"
        response = requests.get(endpoint)
        response.raise_for_status()
        response_json = response.json()
        generated_names = response_json["contents"]["names"]
        return generated_names
