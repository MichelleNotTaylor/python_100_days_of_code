import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

def compare(user_score, computer_score): 
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "Lose, bust"
    elif computer_score > 21:
        return "Win, opponent busted" 
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    end_game = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not end_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User cards: {user_cards} User score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_game = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                end_game = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(compare(user_score, computer_score))
        print(f"Final user score: {user_score}")
        print(f"Final computer score: {computer_score}")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
