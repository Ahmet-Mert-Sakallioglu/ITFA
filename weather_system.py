# weather_system.py
"""
Forest Fire Reinforcement Learning Project : ITFA

Author: Ahmet Mert Sakallıoğlu
"""
import random

class WeatherSystem:

    def __init__(self):

        self.wind_speed= random.uniform(0, 30)  # Rüzgar hızı (km/s)

        self.wind_direction = random.choice([
            "N",
            "S",
            "E",
            "W",
            "NE",
            "NW",
            "SE",
            "SW"
        ])

        self.humidity = random.uniform(20, 80)

        self.temperature = random.uniform(15, 45)

    def update(self):

        self.wind_speed += random.uniform(-2, 2)

        self.wind_speed = max(
            0,
            min(40, self.wind_speed)
        )

        self.temperature += random.uniform(-1, 1)

        self.humidity += random.uniform(-3, 3)

        self.humidity = max(
            10,
            min(100, self.humidity)
        )

    def get_weather_state(self):

        return {
            "wind_speed": self.wind_speed,
            "wind_direction": self.wind_direction,
            "humidity": self.humidity,
            "temperature": self.temperature
        }
