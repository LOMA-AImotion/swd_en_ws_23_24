import random
# from random import randint, choice, seed

# make random generator deterministic / fixed
# random.seed(42)

die = ["."*i for i in range(1, 7)]
thrown = random.choice(die)

print("The result is: ", thrown)