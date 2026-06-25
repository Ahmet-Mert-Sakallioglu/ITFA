# fire_simulation.py
"""
Forest Fire Reinforcement Learning Project : ITFA

Author: Ahmet Mert Sakallıoğlu
"""

import numpy as np
import random

from config import *
from weather_system import WeatherSystem


class FireSimulation:

    def __init__(self):

        self.weather = WeatherSystem()
        self.reset()

    def reset(self):

        self.grid = np.ones((GRID_SIZE, GRID_SIZE), dtype=int)

        for _ in range(INITIAL_FIRE_COUNT):

            x = random.randint(0, GRID_SIZE-1)
            y = random.randint(0, GRID_SIZE-1)

            self.grid[x, y] = BURNING

        self.step_count = 0

        return self.grid

    def spread(self):

        new_grid = self.grid.copy()

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):

                if self.grid[x, y] == BURNING:

                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:

                            nx, ny = x+dx, y+dy

                            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:

                                if self.grid[nx, ny] == FOREST:

                                    prob = BASE_SPREAD_PROBABILITY

                                    prob *= (1 + self.weather.wind_speed / 30)

                                    if random.random() < prob:

                                        new_grid[nx, ny] = BURNING

                    new_grid[x, y] = BURNT

        # SPOT FIRE (yeni yangın çıkışı)
        if random.random() < 0.02:

            sx = random.randint(0, GRID_SIZE-1)
            sy = random.randint(0, GRID_SIZE-1)

            new_grid[sx, sy] = SPOT_FIRE

        self.grid = new_grid

    def step(self):

        self.spread()
        self.weather.update()
        self.step_count += 1

        return self.grid

    def is_done(self):

        return self.step_count >= MAX_EPISODE_STEPS
