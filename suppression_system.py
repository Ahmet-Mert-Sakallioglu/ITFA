# suppression_system.py
"""
Forest Fire Reinforcement Learning Project : ITFA

Author: Ahmet Mert Sakallıoğlu
"""

from config import *


class SuppressionSystem:

    def __init__(self):

        self.history = []

    def apply_suppression(self, grid, targets, vehicles):

        """
        targets: [(x,y)]
        vehicles: list of Vehicle objects
        """

        updated_grid = grid.copy()

        total_power = 0

        for v in vehicles:
            total_power += v.suppression_power

        for (x, y) in targets:

            if updated_grid[x, y] == BURNING:

                if total_power > 0:

                    updated_grid[x, y] = FOREST

        self.history.append({
            "targets": targets,
            "power": total_power
        })

        return updated_grid
