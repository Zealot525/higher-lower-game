# randomly select 2 items from the list
import random
from game_data import data
from art import logo, vs
from replit import clear
choice_1 = random.randint(0, len(data) - 1)
choice_A = data[choice_1]
choice_2 = random.randint(0, len(data) - 1)
choice_B = data[choice_2]
score = 0

# comparing A to B
def comparing(A, B):
    if choice_A['follower_count'] > choice_B['follower_count']:
        return "A"
    elif choice_A['follower_count'] < choice_B['follower_count']:
        return "B"

end = False
while not end:
    # displaying the two list
    print(logo)
    print(f"Your score: {score}")
    print(f"Compare A: {choice_A['name']}, a {choice_A['description'].lower()}, from {choice_A['country']}")
    print(vs)
    print(f"Against B: {choice_B['name']}, a {choice_B['description'].lower()}, from {choice_B['country']}")
    
    # asking the user to select the option
    while True:
        user_choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()
        if user_choice != "A" and user_choice != "B":
            print("Only A or B is allowed!")
        else:
            break
    
    # comparing user choice to the correct answer
    if user_choice == comparing(choice_A['follower_count'], choice_B['follower_count']):
        score += 1
        if user_choice == "B":
            choice_A = choice_B
        choice_B = data[random.randint(0, len(data) - 1)]
        while choice_A == choice_B:
            choice_B = data[random.randint(0, len(data) - 1)]
        clear()
    else:
        clear()
        print(logo)
        print(f"Sorry, {choice_A['name']} has {choice_A['follower_count']} million followers, while {choice_B['name']} has {choice_B['follower_count']} million followers.")
        print(f"Your final score is {score}.")
        print("You lose!")
        end = True

# having the same 