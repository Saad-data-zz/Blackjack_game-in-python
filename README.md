
# Blackjack game Program on Python Full Code.

Blackjack - also called '21' - the classic casino card game of luck and skill! Here we made the game in python
with simple code with the help of using basic functions of python.


## Our House Rules for Game

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The the Ace can count as 11 or 1.
- Use the following list as the deck of cards:
- Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.
## How code Works
- Step# 01: Create a deal_card() function that uses the List below to *return* a random card.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

- Step# 02: Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []

- Step# 03: Create a function called calculate_score() that takes a List of cards as input and returns the score. Look up the sum() function to help you do this.

- Step# 04: Inside calculate_score(). We checked for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

- Step# 05: Inside calculate_score(). We checked for an 11 (ace). If the score is already over 21, we removed the 11 and replace it with a 1. We used append() and remove().

- Step# 06: Call the function we created calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

- Step# 07: If the game has not ended, we ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

- Step# 08: The score will need to be rechecked with every new card drawn and the checks in we need to be repeated until the game ends.

- Step# 09: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

- Step# 10: We created a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

- Step# 11: We asked the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from blackjack_art.py.

The score will need to be rechecked with every new card drawn and need to be repeated until the game ends.

## Authors

- [@saad-data] (https://github.com/Saad-data)


## Feedback

If you have any feedback, please reach out to us at syedsaad047@gmail.com

