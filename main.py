from enviroment import Enviroment
from animal import Animal
import random as rnd


env = Enviroment(10)
animals = [Animal([rnd.randint(0, env.dim - 1), rnd.randint(0, env.dim - 1)], env, 3)]
env.generate_food(0.4)
env.print_map()

# starting with only 1 animal, execute the simulation
# every animal takes a decision, then it's executed
# actions: 1 - move, 2 - sensing, 3 - reproduce

for iteration in range(1, 50):
    print("ITERATION: " + str(iteration))
    updated_animals = []
    for animal in animals:
        decision = animal.next_decision()
        if decision == 1:
            animal.move()
        elif decision == 2:
            animal.sensing()
        elif decision == 3:
            updated_animals.append(animal.reproduce())
        if animal.state > 0:
            updated_animals.append(animal)
            print("Animal id " + str(animal.id) + ", state " + str(animal.state))
        else:
            env.map[animal.pos[0], animal.pos[1]] = 0
    env.print_map()
    if iteration % 3 == 0:
        env.generate_food(0.2)
    animals = updated_animals


print("Total population " + str(len(animals)))