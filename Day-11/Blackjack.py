import random
import os
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if (user_score == comp_score): 
        print("Draw")
    elif (comp_score == 0):
        print("You lose!! Opponent has a blackjack")
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You lose"
    elif comp_score > 21:
        return "Opponent went over. You win"
    elif user_score > comp_score: 
        return "You win!!!"
    else: 
        return "You lose"


def play_game():

    print (logo)
    user_cards = []
    computer_cards = []

    # for _ in range(2):           # the reason to use _ is that as no variable is going to be used as we need the for loop to run ONLY twice
    #     user_cards.append(deal_card())
    #     computer_cards.append(deal_card())

    i = 0                                       # the same logic can be used in the while loop instead of the for loop above.
    while i < 2:
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        i += 1


    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if(user_score == 0 or comp_score == 0 or user_score > 21):
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else: 
                is_game_over = True


    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(compare(user_score,comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()