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

from art import logo
from random import choice


def replace_ace(hand):
    """Replaces a value of an ace from 11 to 1"""
    i = hand.index(11)
    hand[i] = 1


def check_winner(user_score, computer_score, immediate_win):
    if not immediate_win:
        if user_score > 21:
            print("You went over. You lose :(")
        elif user_score < computer_score < 22:
            print("You lose :(")
        elif user_score > computer_score:
            print("You win :)")
        else:
            print("You draw.")
    else:
        print("You won by immediate blackjack!")


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)

    player_cards = [choice(cards), choice(cards)]
    cpu_cards = [choice(cards), choice(cards)]

    cpu_score = sum(cpu_cards)
    while cpu_score < 17:
        cpu_cards.append(choice(cards))
        cpu_score = sum(cpu_cards)
        if cpu_score > 21 and 11 in cpu_cards:
            replace_ace(cpu_cards)
            cpu_score = sum(cpu_cards)

    player_score = sum(player_cards)

    if player_score != 21:
        won_by_blackjack = False
        keep_hitting = True
        while keep_hitting:

            print(f'    Your cards: {player_cards}, current score: {player_score}')
            print(f"    Computer's first card: {cpu_cards[0]}")
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if hit == 'y':
                player_cards.append(choice(cards))
                player_score = sum(player_cards)
                if player_score > 21 and 11 in player_cards:
                    replace_ace(player_cards)
                    player_score = sum(player_cards)
                elif player_score >= 21:
                    keep_hitting = False
            else:
                keep_hitting = False
    else:
        won_by_blackjack = True

    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {cpu_cards}, final score: {cpu_score}")

    check_winner(player_score, cpu_score, won_by_blackjack)

    play_again = input("Do you want to play another hand of Blackjack? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        blackjack()
    else:
        print('Thanks for playing!')


blackjack()
