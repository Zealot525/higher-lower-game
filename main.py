# randomly select 2 items from the list
import random
from game_data import data
choice_1 = random.randint(0, len(data) - 1)
choice_A = data[choice_1]
choice_2 = random.randint(0, len(data) - 1)
choice_B = data[choice_2]

# comparing A to B
def comparing(A, B):
    if choice_A['follower_count'] > choice_B['follower_count']:
        return "A"
    elif choice_A['follower_count'] < choice_B['follower_count']:
        return "B"

# displaying the two list
print(f"Compare A: {choice_A['name']}, a {choice_A['description'].lower()}, from {choice_A['country']}")
print(f"Against B: {choice_B['name']}, a {choice_B['description'].lower()}, from {choice_B['country']}")
print(f"A: {choice_A['follower_count']}, B: {choice_B['follower_count']}")

# asking the user to select the option
user_choice = input("Who has more followers on Instagram? Type 'A' or 'B': ")

# comparing user choice to the correct answer
if user_choice == comparing(choice_A['follower_count'], choice_B['follower_count']):
    if user_choice == "B":
        choice_A = choice_B
    choice_B = data[random.randint(0, len(data) - 1)]
else:
    print(f"Sorry, {choice_A['name']} has {choice_A['follower_count']} million followers, while {choice_B['name']} has {choice_B['follower_count']} million followers.")
    print("You lose!")