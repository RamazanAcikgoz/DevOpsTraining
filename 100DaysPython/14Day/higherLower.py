import art
from gameData import data
import vs
import random

# TODO-1 : Print logo
print(art.logo)

# TODO-2 : Print random person from dict with value
# Kim Kardashan, a reality tv personality ... 
def random_picker():
    random_name_one = random.choice(data)
    print(f"Compare A: {random_name_one.get('name')}, a/an {random_name_one.get('description')}, from {random_name_one.get('country')}")
    return random_name_one
    

person_a = random_picker()

# TODO-3 : Print VS.
print(vs.logo)

# TODO-4 : Print random person_two from dict with value
person_b = random_picker()
if person_a.get('name') == person_b.get('name'):
    person_b = random_picker()


# TODO-5 : Compare () : Who has more followers? Type 'A' or 'B':
choice = input("Who has more followers? Type 'A' or 'B' : ").lower()


# TODO-6 : If true : You'r right! Current score : 1. keep correct answer and choose random another person
def compare(a, b, option):
    score = 0
    if a.get('follower_count') > b.get('follower_count') and option == 'a':
        score += 1
        print(f"You're right! Current score : {score}.")
        return f"Compare A: {a.get('name')}, a/an {a.get('description')}, from {a.get('country')}"
    elif b.get('follower_count') > a.get('follower_count') and option == 'b':
        score += 1
        print(f"You're right! Current score : {score}.")
        return f"Compare A: {b.get('name')}, a/an {b.get('description')}, from {b.get('country')}"
    elif a.get('follower_count') > b.get('follower_count') and option == 'b':
        print(f"Sorry, that's wrong! Final score : {score}.")
        return False
    elif b.get('follower_count') > a.get('follower_count') and option == 'a':
        print(f"Sorry, that's wrong! Final score : {score}.")
        return False
    else:
        return "Enter correct choice 'A' or 'B'"

def guessing():
    score = 0
    is_true = True
    while is_true:
        print(art.logo)
        person_a = random_picker()
        print(vs.logo)
        person_b = random_picker()
        if person_a.get('name') == person_b.get('name'):
            person_b = random_picker()
        choice = input("Who has more followers? Type 'A' or 'B' : ").lower()
        compare(person_a, person_b, choice)
        if compare == False:
            is_true = False

print(guessing())