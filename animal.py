import random as rnd
import copy


class Animal:

    ID = 0

    def __init__(self, starting_pos, enviroment, starting_state):
        self.id = Animal.ID + 1
        Animal.ID += 1
        self.pos = starting_pos
        self.env = enviroment
        enviroment.update_animal_position(self.pos, self.pos)
        self.state = starting_state

    def move(self):
        steps = 5
        self.state -= 1
        old_pos = copy.deepcopy(self.pos)
        for _ in range(steps):
            new_x = self.pos[0] + rnd.randint(-1, 1)
            new_y = self.pos[1] + rnd.randint(-1, 1)
            while not self.env.check_safe(new_x, new_y):
                new_x = self.pos[0] + rnd.randint(-1, 1)
                new_y = self.pos[1] + rnd.randint(-1, 1)
            if self.env.map[new_x, new_y] == 1:
                self.state = min(self.state + 1, 4)
                self.env.map[new_x, new_y] = 0
            self.pos = [new_x, new_y]
        self.env.update_animal_position(self.pos, old_pos)

    def sensing(self):
        self.state -= 1
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x = self.pos[0] + i
                y = self.pos[1] + j
                if self.env.check_safe(x, y) and self.env.map[x, y] == 1:
                    self.env.map[self.pos[0] + i, self.pos[1] + j] = 0
                    self.state = min(self.state + 1, 4)

    def reproduce(self):
        self.state -= 2
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x = self.pos[0] + i
                y = self.pos[1] + j
                if self.env.check_safe(x, y):
                    return Animal([x, y], self.env, 2 + self.env.map[x, y])

    def next_decision(self):
        return rnd.randint(1, 2)
