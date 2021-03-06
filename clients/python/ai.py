"""
This is the file that should be used to code your AI.
"""
import random
from planar import Vec2

from game.models import *


class AI:
    def __init__(self):
        pass

    def step(self, game: Game):
        """
        Given the state of the 'game', decide what your cells ('game.me.cells')
        should do.

        :param game: Game object
        """

        print("Tick #{}".format(game.time_left))

        for cell in game.me.cells:
            distance = cell.position.distance_to(cell.target)

            if distance < 10:
                target = Vec2(random.randint(0, game.map.width), random.randint(0, game.map.height))

                cell.move(target)
