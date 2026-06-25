# vehicles.py
"""
Forest Fire Reinforcement Learning Project : ITFA

Author: Ahmet Mert Sakallıoğlu
"""

from config import *


class Vehicle:

    def __init__(self, name, suppression_power, speed):

        self.name = name
        self.suppression_power = suppression_power
        self.speed = speed

        self.available = True


class FireTruck(Vehicle):

    def __init__(self):

        super().__init__(
            "FireTruck",
            FIRETRUCK_SUPPRESSION,
            speed=3
        )


class Helicopter(Vehicle):

    def __init__(self):

        super().__init__(
            "Helicopter",
            HELICOPTER_SUPPRESSION,
            speed=6
        )


class Aircraft(Vehicle):

    def __init__(self):

        super().__init__(
            "Aircraft",
            AIRCRAFT_SUPPRESSION,
            speed=10
        )
