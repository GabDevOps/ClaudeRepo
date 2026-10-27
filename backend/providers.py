"""Property providers: where the backend gets its houses from.

Every provider has the same `search(...)` method, so the rest of the app
does not care whether the data is fake or comes from the real idealista API.
"""

SAMPLE_HOUSES = [
    {"title": "Bright flat near the river", "city": "Lisboa", "price": 285000, "rooms": 2, "size_m2": 78},
    {"title": "Family house with garden", "city": "Lisboa", "price": 540000, "rooms": 4, "size_m2": 160},
    {"title": "Studio in the old town", "city": "Porto", "price": 165000, "rooms": 1, "size_m2": 40},
    {"title": "Renovated 3-bedroom", "city": "Porto", "price": 310000, "rooms": 3, "size_m2": 105},
    {"title": "Penthouse with terrace", "city": "Madrid", "price": 690000, "rooms": 3, "size_m2": 130},
    {"title": "Cosy flat close to metro", "city": "Madrid", "price": 240000, "rooms": 2, "size_m2": 65},
]


class MockProvider:
    """Fake idealista: filters the sample houses above."""

    def search(self, city, max_price, min_rooms):
        return [
            house for house in SAMPLE_HOUSES
            if house["city"].lower() == city.lower()
            and house["price"] <= max_price
            and house["rooms"] >= min_rooms
        ]


class IdealistaProvider:
    """Placeholder for the official idealista API (needs an API key).

    See https://developers.idealista.com – to be implemented once we have a key.
    """

    def search(self, city, max_price, min_rooms):
        raise NotImplementedError("idealista API not connected yet")
