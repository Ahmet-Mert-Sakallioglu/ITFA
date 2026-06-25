# terrain_generator.py
# ==================================================
# Forest Fire Reinforcement Learning Project
# Author: Ahmet Mert Sakallıoğlu
# ======
import numpy as np
from config import *

class TerrainGenerator:

    def __init__(self, grid_size=GRID_SIZE):
        self.grid_size = grid_size

    def generate_fuel_map(self):

        fuel_map = np.random.uniform(
            MIN_FUEL,
            MAX_FUEL,
            (self.grid_size, self.grid_size)
        )

        return fuel_map

    def generate_elevation_map(self):

        elevation = np.random.rand(
            self.grid_size,
            self.grid_size
        )

        elevation = self.smooth(elevation)

        return elevation

    def generate_forest_map(self):

        forest = np.ones(
            (self.grid_size, self.grid_size),
            dtype=np.int32
        )

        return forest

    def smooth(self, data, iterations=5):

        result = data.copy()

        for _ in range(iterations):

            result = (
                result +
                np.roll(result, 1, axis=0) +
                np.roll(result, -1, axis=0) +
                np.roll(result, 1, axis=1) +
                np.roll(result, -1, axis=1)
            ) / 5

        return result
