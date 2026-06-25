# fire_simulation.py
"""
Forest Fire Reinforcement Learning Project : ITFA

Author: Ahmet Mert Sakallıoğlu
"""

import numpy as np
import random

from config import *
from terrain_generator import TerrainGenerator
from weather_system import WeatherSystem


class FireSimulation:

    def __init__(self):

        self.grid_size = GRID_SIZE

        self.terrain = TerrainGenerator()
        self.weather = WeatherSystem()

        self.reset()

    def reset(self):

        self.grid = self.terrain.generate_forest_map()
        self.fuel_map = self.terrain.generate_fuel_map()
        self.elevation_map = self.terrain.generate_elevation_map()

        self.weather = WeatherSystem()

        self.current_step = 0

        self._ignite_initial_fires()

        return self.grid

    def _ignite_initial_fires(self):

        for _ in range(INITIAL_FIRE_COUNT):

            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)

            self.grid[x, y] = BURNING

    def get_neighbors(self, x, y):

        neighbors = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:

                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                    neighbors.append((nx, ny))

        return neighbors

    def compute_spread_probability(self, x, y, nx, ny):

        prob = BASE_SPREAD_PROBABILITY

        fuel = self.fuel_map[nx, ny]
        elevation_diff = self.elevation_map[nx, ny] - self.elevation_map[x, y]

        wind_factor = self.weather.wind_speed / 30.0
        humidity_factor = self.weather.humidity / 100.0

        prob *= fuel
        prob *= (1 + wind_factor)

        if elevation_diff > 0:
            prob *= 1.2

        prob *= (1 - 0.5 * humidity_factor)

        return min(max(prob, 0.0), 1.0)

    def step(self):

        new_grid = self.grid.copy()

        burning_cells = np.argwhere(self.grid == BURNING)

        for x, y in burning_cells:

            for nx, ny in self.get_neighbors(x, y):

                if self.grid[nx, ny] != FOREST:
                    continue

                p = self.compute_spread_probability(x, y, nx, ny)

                if np.random.random() < p:
                    new_grid[nx, ny] = BURNING

            new_grid[x, y] = BURNT

        self.grid = new_grid

        self.weather.update()
        self.current_step += 1

        return self.grid

    def is_fire_active(self):

        return np.any(self.grid == BURNING)

    def get_state(self):

        return self.grid.copy()
