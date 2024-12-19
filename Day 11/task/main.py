import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def compare(u_score, c_score):
    if c_score == u_score:
        print("It's a draw.")
    elif c_score == 0:
        print("The computer got blackjack!")
    elif u_score == 0:
        print("The user got blackjack!")
    elif u_score > 21:
        print("The user loses the game!")
    elif c_score > 21:
        print("The computer loses the game!")
    else:
        if u_score > c_score:
            print("The user wins the game.")
        else:
            print("The computer wins the game.")

def play_game():
    print(art.logo)

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(list_cards):
        total_score = sum(list_cards)
        if total_score == 21 and len(list_cards) == 2:
            return 0

        if 11 in list_cards and sum(list_cards) > 21:
            list_cards.remove(11)
            list_cards.append(1)

        return sum(list_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            game_continue = input("Do you want to draw another card to your hand. Type 'yes' or 'no'. ")
            if game_continue == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_game()
