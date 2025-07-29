import random as rand
numbers=[11,2,3,4,5,6,7,8,9,10,10,10,10]

#pick a random number from the list
def pick_random_number():
    return rand.choice(numbers)

def ace(cards):
    if 11 in cards and sum(cards) > 21:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
            return sum(cards)
    else:
        return sum(cards)

#cards for the user and dealer

def black_jack():
    user_cards=[]
    dealer_cards=[]

    consent = input("Welcome to Black Jack! Do you want to play? (y/n): ").lower()
    if consent == "y":
        
        user_cards.append(pick_random_number())
        user_cards.append(pick_random_number())
        user_sum = ace(user_cards)
        print(f"Your cards: {user_cards} and the sum is {user_sum}")
        if user_sum > 21:
            print("You Lose!")
            print("\n"*5)
            black_jack()

        dealer_cards.append(pick_random_number())
        dealer_sum = ace(dealer_cards)
        print(f"Dealer's card: {dealer_cards[0]} and the sum is {dealer_sum}")

        play = input("hit or stay? (h/s): ").lower()
        while play == "h":
            user_cards.append(pick_random_number())
            user_sum = ace(user_cards)
            print(f"Your cards: {user_cards} and the sum is {user_sum}")
            if user_sum > 21:
                print("You Lose!")
                print("\n"*5)
                black_jack()
            play = input("hit or stay? (h/s): ").lower()
        
        if user_sum <= 21:
            dealer_cards.append(pick_random_number())
            dealer_sum = ace(dealer_cards)
            print(f"Dealer's cards: {dealer_cards} and the sum is {dealer_sum}")
            while dealer_sum < 13:
                dealer_cards.append(pick_random_number())
                dealer_sum = ace(dealer_cards)
                print(f"Dealer's cards: {dealer_cards} and the sum is {dealer_sum}")
            if dealer_sum > 21:
                print("Dealer busts! You win!")
                print("\n"*5)
                black_jack()
            elif dealer_sum > user_sum:
                print("Dealer wins!")
                print("\n"*5)
                black_jack()
            elif dealer_sum < user_sum:
                print("You win!")
                print("\n"*5)
                black_jack()
            else:
                print("It's a tie!")
                print("\n"*5)
                black_jack()

black_jack()