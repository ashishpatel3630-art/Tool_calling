def get_weather(city: str) -> dict:
    """
    Get weather information for a city.
    """

    weather = {

        "Bhopal": {
            "temperature": 28,
            "condition": "Cloudy",
            "humidity": 70
        },

        "Delhi": {
            "temperature": 35,
            "condition": "Sunny",
            "humidity": 45
        },

        "Mumbai": {
            "temperature": 30,
            "condition": "Humid",
            "humidity": 80
        },

        "Indore": {
            "temperature": 29,
            "condition": "Clear",
            "humidity": 55
        }
    }

    return weather.get(
        city,
        {
            "error": f"No weather data for {city}"
        }
    )