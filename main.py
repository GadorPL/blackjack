# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from art import logo
from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)

player_cards = [choice(cards), choice(cards)]
cpu_cards = [choice(cards), choice(cards)]


keep_hitting = True
while keep_hitting:
    player_score = sum(player_cards)
    print(f'    Your cards: {player_cards}, current score: {player_score}')
    print(f"    Computer's first card: {cpu_cards[0]}")
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if hit == 'y':
        player_cards.append(choice(cards))
    else:
        print(f"    Your final hand: {player_cards}, final score: {player_score}")

        cpu_score = sum(cpu_cards)
        while cpu_score < 17:
            cpu_cards.append(choice(cards))

        print(f"    Computer's final hand: {cpu_cards}, final score: {cpu_score}")
        if player_score > cpu_score:
            print(f"You win :)")
        elif player_score < cpu_score:
            print(f"You lose :(")
        else:
            print(f"You draw.")
        keep_hitting = False
