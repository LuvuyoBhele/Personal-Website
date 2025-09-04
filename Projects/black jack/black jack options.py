import random as rand
import numpy as np
import pandas as pd
numbers=[11,2,3,4,5,6,7,8,9,10,10,10,10]

#pick a random number from the list
def pick_random_number():
    return rand.choice(numbers)

def ace(cards):
    #11 acts as an ace but if the sum of all cards gives you more than 21 then it goes back to being 1 
    if 11 in cards and sum(cards) > 21:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
        return sum(cards)
    else:
        return sum(cards)

#cards for the user and dealer
"""
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
"""


#black_jack()

#simulation for game
def hitOrStay(userSum, safeHit):
    #this function takes the final scores of game [user score, dealer score]
    #and checks which player has the highest score and tell you whether it's a win or lose
    if userSum > safeHit:
        return("s")
    elif userSum < safeHit:
        return("h")

def black_jack_sim(numberOfGames, safeHit):
    games = [] #we store info about all the games
    i=0 #keeps number of games
    while i < numberOfGames:
        #initialize game
        result = ""
        user_cards = []
        dealer_cards = []
        #the user must get his two first cards
        user_cards.append(pick_random_number())
        user_cards.append(pick_random_number())

        #first choice
        user_sum = ace(user_cards) #ACE STRATEGY FOR DEALER

        #print(f"Your cards: {user_cards} and the sum is {user_sum}")
        if user_sum > 21:
            result = "lose"
            #print(f"You "+ result +"!")
            games.append([user_cards,dealer_cards, result])
            i += 1
        elif user_sum == 21:#NEEDS IMPROVEMENT CAUSE IT'S NOT ACCURATE WITH RULES. WHAT IF DEALER GETS 21 
            result = "win"
            #print(f"You "+ result +"!")
            games.append([user_cards,dealer_cards, result])
            i += 1

        else: #LOOKING AT CASE WHEN THE FIRST TWO CARDS SUM IS < 21
            dealer_cards.append(pick_random_number()) #DEALER GETS HIS FIRST CARD
            dealer_sum = ace(dealer_cards) #ACE STRATEGY FOR DEALER
            #print(f"Dealer's card: {dealer_cards[0]} and the sum is {dealer_sum}")

            #first game decsion must be made by user 
            #implement strategy here
            play = hitOrStay(user_sum, safeHit)


            while play == "h": 
                #this is the users turn
                user_cards.append(pick_random_number()) #user picks third card
                user_sum = ace(user_cards) #ACE STRATEGY FOR USER
                #print(f"Your cards: {user_cards} and the sum is {user_sum}")
                #first game decsion made by user 
                play = hitOrStay(user_sum, safeHit)#USER STRATEGY
            #the users TURN is done

            if user_sum > 21:
                    result = "lose"
                    #print(f"You "+ result +"!")
                    games.append([user_cards,dealer_cards, result])
                    i += 1

            else:
                dealer_cards.append(pick_random_number()) #NOW THE DEALER GETS TO PLAY THEIR SECOND CARD
                dealer_sum = ace(dealer_cards) #dealers ace strategy
                #print(f"Dealer's cards: {dealer_cards} and the sum is {dealer_sum}")
                #dealer strategy 
                while dealer_sum < 21:
                    #work on this game logic
                    dealer_cards.append(pick_random_number())#DEALER GETS 3RD CARD 
                    dealer_sum = ace(dealer_cards)#Dealer ace strategy
                    #print(f"Dealer's cards: {dealer_cards} and the sum is {dealer_sum}")
                    if dealer_sum > 21:
                        result = "win"
                        #print(f"you " +  result + "!")
                        games.append([user_cards,dealer_cards,result])
                        i += 1

                    elif dealer_sum > user_sum:
                        result = "lose"
                        #print(f"you " +  result + "!")
                        games.append([user_cards,dealer_cards,result])
                        i += 1

                    elif dealer_sum < user_sum:
                        result = "win"
                        #print(f"you " +  result + "!")
                        games.append([user_cards,dealer_cards,result])
                        i += 1

                    else:
                        result = "push"
                        games.append([user_cards,dealer_cards,result])
                        i += 1
    # Convert games to DataFrame
    df = pd.DataFrame(games, columns=['user_cards', 'dealer_cards', 'result'])
    return df


df = black_jack_sim(10000, 21)
print(df)

# Save DataFrame to Excel at your specified location
df.to_excel(r"C:\Users\27671\OneDrive\Documents\Web.Dev.Proj\My Portfolio\Projects\black jack\Data dump.xlsx", index=False, sheet_name="thresh hit 14")