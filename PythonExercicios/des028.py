from random import randint
from time import sleep
print('Olá!\nVamos brincar de adivinhação?!')
print('-.-º' * 20)
sleep(0.5)
num_machine = randint(0,5)
num_custumer = int(input('Pensei em um número entre 0 e 5, tente acertar qual foi: \n'))
print('Processando...')
sleep(1.5)
if num_custumer == num_machine:
    print('Parabéns, você acertou!')
else:
    print('Sinto muito, você errou! \nO número sorteado pela máquina foi {}'.format(num_machine))
