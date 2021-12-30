from random import randint
from time import sleep
print('Olá!\nVamos brincar de adivinhação?!')
print('-.-.' * 20)
num_machine = randint(0,10)
num_customer = int(input('Pensei em um número entre 0 e 10, tente acertar qual foi: \n'))
tentativas = 1
print('Processando...')
sleep(1.0)
while num_customer != num_machine:
    if num_customer < num_machine:
        num_customer = int(input('Um pouco mais... \nTente novamente: '))
        tentativas += 1
    if num_customer > num_machine:
        num_customer = int(input('Um pouco menos... \nTente novamente: '))
        tentativas += 1
print('Parabéns, você acertou! \nForam necessárias {} tentativas para acertar.'.format(tentativas))
