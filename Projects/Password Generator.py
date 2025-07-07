#random number generator
import random
#user can input how many characters they want in their password
#user can specify how many letters + how many numbers + how many symbols they want in password

letters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers =[str(i) for i in range(0,10)]
symbols =['!','@','#','$','%','&','(',')','*','+']

total_char=int(input('How many characters should your password be? '))
total_letters = int(input(f'How many letters should be in the password(0-{total_char})?'))
total_numbers = int(input(f'How many numbers should be in the password(0-{total_char-total_letters})?'))
total_symbols = int(input(f'How many symbols should be in the password(0-{total_char-total_letters-total_numbers})?'))

#Easy challenge based on the specifications given by the user generate a password in the same order
password_char = []
#generating the first letters requires a randomistion of letters by the number of total 
for i in range(0,int(total_letters)):
    random_letter = letters[random.randint(0,len(letters)-1)]
    password_char.append(random_letter)
for i in range(0,int(total_numbers)):
    random_number = numbers[random.randint(0,len(numbers)-1)]
    password_char.append(str(random_number))
for i in range(0,int(total_symbols)):
    random_symbol = symbols[random.randint(0,len(symbols)-1)]
    password_char.append(random_symbol)
    

#password = ''.join(password_char)
#print(f'Your password is {password}')

#Hard challenge! Randomise the order
random.shuffle(password_char)
password = ''.join(password_char)
print(f'Your password is {password}')