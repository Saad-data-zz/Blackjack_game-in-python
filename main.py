############### Blackjack Project #####################

import random
from blackjack_art import logo
from replit import clear


# TODO#01 : Deal both user and computer a starting hand of 2 random card values.

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# TODO#02 : Detect when computer or user has a blackjack. (Ace + 10 value card)
# TODO#03 : If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# TODO#04 : If computer gets blackjack, then the user loses (even if the user also has a blackjack).
# If the user gets a blackjack, then they win (unless the computer also has a blackjack).
# Calculate the user's and computer's scores based on their card values.

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Your values of cards went over. You lose. GAME OVER 😤"
    if user_score == computer_score:
        return "Draw🙃"
    elif computer_score == 0:
        return "Lose, Opponent has BlackJack😱"
    elif user_score == 0:
        return "Wins with the BlackJack😎"
    elif user_score > computer_score:
        return "You Win!😃"
    elif user_score > 21:
        return "Your value of cards went over! You lose😭"
    elif computer_score > 21:
        return "Dealer value of card went over! You Win😃!"
    else:
        return "Dealer Wins! You lose😤"


def play_game():
    print(logo)
    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"  Your Cards: {user_score}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card()
            # function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Ask the user if they want to restart the game. If they answer yes,
# clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
