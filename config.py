# config.py
"""
Forest Fire Reinforcement Learning Project : ITFA

Author: Ahmet Mert Sakallıoğlu
"""

GRID_SIZE = 64

EMPTY = 0
FOREST = 1
BURNING = 2
BURNT = 3
SPOT_FIRE = 4

INITIAL_FIRE_COUNT = 3

MAX_EPISODE_STEPS = 300

BASE_SPREAD_PROBABILITY = 0.25

MIN_FUEL = 0.2
MAX_FUEL = 1.0

WIND_MAX = 30

NUM_AGENTS = 1
