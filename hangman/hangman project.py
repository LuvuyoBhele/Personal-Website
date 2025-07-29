
import random
import names_hangman
from names_hangman import names


lives=6
chosen_word=random.choice(names)
#print(chosen_word)

placeholder = ['_' for i in range(len(chosen_word))]
placeholder_word= ''.join(placeholder)
guessed_letters = []
#print(placeholder_word)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


while chosen_word!=placeholder_word and  lives!=0:
    #print(chosen_word)
    print(placeholder_word)
    print(HANGMANPICS[6-lives])
    print(f'number of lives left {lives}')

    guess = input('guess the letter:').lower()
    while guess in guessed_letters:
      print("you've guessed this letter please pick a different letter")
      guess = input('guess the letter:').lower()
    guessed_letters.append(guess)

    print(guess)
    hits=0

    for i in range(len(chosen_word)):
        if  chosen_word[i] == guess[0]:
            #not if there's no guess you'll get an out of range error\m9
            #print('true')
            placeholder[i] = guess[0]
            placeholder_word= ''.join(placeholder)
            hits +=1
            #print(placeholder_word)
        #else:
            #print('wrong')
            #print(chosen_word[i])
    if hits == 0:
        lives-=1
        #print(f'number of lives left {lives}')
        
    if  lives==0:
        print(f'number of lives left {lives}')
        print('you lose')
        print(f'the word is {chosen_word}')
    if chosen_word == placeholder_word:
        print('you win')

