from enviroment import Enviroment
from animal import Animal
import random as rnd
from mdp_function import compute_policies
import matplotlib.pyplot as plt


INIT_FOOD_PROB = 0.6
REGEN_FOOD_PROB = 0.2
SQUARE_EDGE = 30

env = Enviroment(SQUARE_EDGE)
Animal.POLICY_ARRAY = compute_policies()
animals = [Animal([rnd.randint(0, env.dim - 1), rnd.randint(0, env.dim - 1)], env, 2)]
env.generate_food(INIT_FOOD_PROB)
env.print_map()

# starting with only 1 animal, execute the simulation
# every animal takes a decision, then it's executed
# actions: 1 - move, 2 - sensing, 3 - reproduce


population_array = []
for iteration in range(1, 150):
    print("ITERATION: " + str(iteration))
    updated_animals = []
    population_dimension = 0
    for animal in animals:
        decision = animal.next_decision()
        if decision == 1:
            animal.move()
        elif decision == 2:
            animal.sensing()
        elif decision == 3:
            updated_animals.append(animal.reproduce())
            population_dimension += 1
        if animal.state > 0:
            updated_animals.append(animal)
            population_dimension += 1
        else:
            env.map[animal.pos[0], animal.pos[1]] = 0
    print("Population dimension: " + str(population_dimension))
    population_array.append(population_dimension)
    # env.print_map()
    if iteration % 3 == 0:
        env.generate_food(REGEN_FOOD_PROB)
    animals = updated_animals


plt.plot(range(len(population_array)), population_array)
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Initial food prob: " + str(INIT_FOOD_PROB) + ". Regen prob: " + str(REGEN_FOOD_PROB) + ". Map dimension: " + str(SQUARE_EDGE**2))
plt.show()
