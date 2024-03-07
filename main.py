# randomly select 2 items from the list
import random
from game_data import data
choice_1 = random.randint(0, len(data) - 1)
choice_A = data[choice_1]
choice_2 = random.randint(0, len(data) - 1)
choice_B = data[choice_2]

# displaying the two list
print(f"Compare A: {choice_A['name']}, a {choice_A['description'].lower()}, from {choice_A['country']}")
print(f"Against B: {choice_B['name']}, a {choice_B['description'].lower()}, from {choice_B['country']}")