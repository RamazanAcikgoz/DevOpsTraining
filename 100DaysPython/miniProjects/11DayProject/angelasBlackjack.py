import random
import art

def deal_cards():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2: # it is mean just 2 cards
        return 0 # it mean someone get just blackjack
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    '''Compare the user and computer scores'''
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    # it is in advance to block a bug between while loops
    # 0 it mean blackjack in the game 
    # that's why we assign -1 to computer score
    # Similar situation with user_score
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    
    # Computer turn
    # if it is less then 17 it should draw more card as it is rule
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == "y":
    print("\n" * 20)
    play_game()