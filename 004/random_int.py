import random
import math

rand = random.randint(1, 6)
print(rand)

rand2 = random.random()
rand2 = math.floor(rand2 * 6 + 1)
print(rand2)