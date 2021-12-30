from time import sleep
from random import randint

itens = ('Rock', 'Paper', 'Scissors')
print('{:-^40}'.format(' JO KEN PO '))
print('Hello! How about a little game?')
print('See your options')
print('''[0] Rock
[1] Paper
[2] Scissors''')
player = int(input('Choose an option and lets go:'))
computer = randint(0,2)

if player < 0 or player > 2:
    print('\033[1;31mOh, man. This is a invalid option! \nPlease, choose a number between 0, 1 or 2.')

else:

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!')
    sleep(1)

    print('Player chose {}'.format(itens[player]))
    print('Computer chose {}'.format(itens[computer]))

    if player == computer:
        print("\033[1;33mDRAW")
    elif player == 0 and computer == 1:
        print('\033[31mComputer WINS!')
    elif player == 1 and computer == 2:
        print('\033[31mComputer WINS!')
    elif player == 2 and computer == 0:
        print('\033[31mComputer WINS!')
    else:
        print('\033[1;32mPlayer WINS!')