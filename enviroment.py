import numpy as np
import random as rnd
from animal import Animal

# map is a 2-D numpy array
# 0 - free
# 1 - food
# 2 - animal


class Enviroment:

    def __init__(self, dimension):
        self.dim = dimension
        self.map = np.zeros((dimension, dimension))

    def update_animal_position(self, new_pos, old_pos):
        self.map[old_pos[0], old_pos[1]] = 0
        self.map[new_pos[0], new_pos[1]] = 2

    def generate_food(self, prob):
        for row in range(self.dim):
            for col in range(self.dim):
                if self.map[row, col] == 0 and rnd.random() < prob:
                    self.map[row, col] = 1

    def check_safe(self, x, y):
        if x < 0 or y < 0 or x >= self.dim or y >= self.dim or self.map[x, y] == 2:
            return False
        return True

    def print_map(self):
        for row in self.map:
            string = "|"
            for e in row:
                if e == 0:
                    string += "   "
                elif e == 1:
                    string += " + "
                elif e == 2:
                    string += " A "
            print(string + "|")
        print("\n \n")
