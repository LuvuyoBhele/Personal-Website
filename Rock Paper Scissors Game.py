#Goal is to create a game of rock paper scissors where the computer is the opponent.
#How the game works:
#each player has to choose one of the following weapons; (1)Rock,(2)paper,(3)scissors.
#if user picks rocks=> comp picks (rocks=>tie) or (sci=>win),(pap=lose)
#if user picks paper=> comp picks (rocks=>win) or (sci=>lose),(pap=tie)
#if user picks sci=> comp picks (rocks=>lose) or (sci=>tie),(pap=win)
import random
weapons = ['scissors' 'rock','paper','scissors']
user_weapon=weapons[int(input('(0)Rock,(1)paper,(2)scissors.\nChoose your weapon?'))]
opps_weapon=weapons[random.randint(0,2)]
if user_weapon =='scissors' and opps_weapon == 'scissors':
    print('''You:
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
          
        Computer:
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
''')
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nTie')

elif user_weapon=='scissors' and opps_weapon == 'rock':
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nYou Lose')
    print('''You:
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
          
        Computer:
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')

elif user_weapon=='scissors' and opps_weapon == 'paper':
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nYou Win')
    print('''You:
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
          
        Computer:
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
''')
#consider the case user_weapon = paper
elif user_weapon=='paper' and opps_weapon == 'rock': #user=paper
    print('''You:
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
            Computer:
        ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
          ''')
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nYou Win')

elif user_weapon=='paper' and opps_weapon == 'paper':
      
    print('''You:
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
          Computer:
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
          
          ''')
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nTie')

elif user_weapon=='paper' and opps_weapon == 'scissors':
    print('''You:
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
          Computer:
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
          
          
          ''')
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nYou Lose')
#consider the case user_weapon = rock
elif user_weapon=='rock' and opps_weapon == 'scissors':
     print(''' You:
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
        Computer:
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
        
           ''')
     print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nYou Win')

elif user_weapon=='rock' and opps_weapon == 'rock':
    print(''' You:
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
          Computer:
        ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
        
           ''')
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nTie')

elif user_weapon=='rock' and opps_weapon == 'paper':
    print(''' You:
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
          Computer:
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
        
           ''')
    print('computer throws:'+ opps_weapon +'\nyou throw:'+ user_weapon+'\nYou Lose')