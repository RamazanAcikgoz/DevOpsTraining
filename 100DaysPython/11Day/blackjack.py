import random
import art

# TODO-1: 
# The decs is unlimited in size
# There are no jokers
# The Jack/Queen/King all counts at 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn
# Cards are not removed from the deck as they are drawn
# The computer is the dealer
# The player's score is the sum of the cards in their hand
computer_cards = []
player_cards = []

def score_counter(deck_owner):
    '''It will count sum of numbers of the deck'''
    total_score = sum(deck_owner)
    # for x in deck_owner:
    #     total_score += x
    if 11 in deck_owner and total_score > 21:
        total_score -= 10
    return total_score

def winner_checker(player_score, computer_score):
    '''It will check the winner'''
    if player_score > 21:
        return "Dealer went over. You win!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif player_score == computer_score:
        return "It's a draw!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def status_shower(play_deck, computer_deck):
    '''Display the current status of players'''
    print(f"Your cards: {play_deck}, current score: {score_counter(play_deck)}")
    print(f"Computer's first card: [{computer_deck[0]}]")

def blackjack():
    # card draws
    computer_cards = random.sample(cards,2)
    player_cards = random.sample(cards, 2)

    # Player's turn
    while True:
        status_shower(player_cards, computer_cards)

        # Check if it is bust or Blackjack
        if score_counter(player_cards) == 21:
            return "Blackjack!"
        elif score_counter(player_cards) > 21:
            return "Bust!"

        action = input("Type 'y' to get another card, type 'n' to pass : ").lower()
        if action == "y":
            player_cards.append(random.choice(cards))
        else:
            break
    
    while score_counter(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

    print(f"Your cards: {player_cards}, current score: {score_counter(player_cards)}")
    print(f"Computer's cards: {computer_cards}, final score : {score_counter(computer_cards)}")

    return winner_checker(score_counter(player_cards), score_counter(computer_cards))

if input("Do you want to play Blackjack? Type 'y' or 'n' : ").lower() == 'y':
    print(blackjack())
                