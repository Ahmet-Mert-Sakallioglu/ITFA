# environment.py
"""
Forest Fire Reinforcement Learning Project : ITFA

Author: Ahmet Mert Sakallıoğlu
"""

import numpy as np

from config import *
from fire_simulation import FireSimulation
from vehicles import FireTruck, Helicopter, Aircraft
from suppression_system import SuppressionSystem


class FireEnv:

    def __init__(self):

        self.sim = FireSimulation()
        self.suppression = SuppressionSystem()

        self.vehicles = [
            FireTruck(),
            Helicopter(),
            Aircraft()
        ]

        # observation: grid flatten + weather (basit tutuldu)
        self.observation_space_size = GRID_SIZE * GRID_SIZE + 3

        self.step_count = 0

        self.state = None

    def reset(self):

        grid = self.sim.reset()

        self.step_count = 0

        return self._get_observation(grid)

    def _get_observation(self, grid):

        flat_grid = grid.flatten()

        weather = self.sim.weather.get_state()

        obs = np.concatenate([
            flat_grid,
            np.array(weather)
        ])

        return obs.astype(np.float32)

    def step(self, action):

        """
        action = (x, y) target koordinatı
        """

        x, y = action

        targets = [(int(x), int(y))]
        # eski gridi kopyala
        grid_before = self.sim.grid.copy()

        # simulation step
        self.sim.step()

        # suppression uygula
        new_grid = self.suppression.apply(
            self.sim.grid,
            targets,
            self.vehicles
        )

        self.sim.grid = new_grid

        reward = self._compute_reward(grid_before, new_grid)

        done = self.sim.is_done()

        self.step_count += 1

        return self._get_observation(new_grid), reward, done, {}

    def _compute_reward(self, before, after):

        fire_before = np.sum(before == BURNING)
        fire_after = np.sum(after == BURNING)

        burnt = np.sum(after == BURNT)

        reward = (fire_before - fire_after) * 2 - burnt * 0.1

        return float(reward)
