#goal:
#create a program that calculates the bill shared amongst a group of people

#Specifications:
#1) must include different options for tips
#2)must specify how much each person must pay
def calculate_bill():
    print('Welcome to the tip calculator!')
    bill = float(input('how much is the bill? R'))
    tip = int(input('how much do you want to tip (0%-100%)?'))
    Num_people = int(input('how many people to split the bill? '))
    bill_pp = round(bill*((1+float(tip/100))/Num_people),2)
    print(f'Each person should pay: R{bill_pp}')
    print('\n'*5)
    calculate_bill()

calculate_bill()