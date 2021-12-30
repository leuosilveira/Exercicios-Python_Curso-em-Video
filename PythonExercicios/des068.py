from random import randint
from time import sleep

print('-'*40)
print('Vamos jogar Par ou Impar!')
print('-'*40)

while True:
    user = int(input('Diga um valor entre 0 e 10: '))
    option = str(input('Escolha sua opção: [P/I] ')).strip().upper()
    print('-'*30)
    computer = randint(0,10)
    s = user + computer
    result = s % 2
    for i in range(1,4):
        print('.',end=" ")
        sleep(0.5)

    print(f'Você escolheu {user} e eu escolhi {computer}.')

    if result > 0:
        final = "I"
    else:
        final = "P"

    if option == final:
        print('Parabéns, você venceu!')
        countwins =+ 1
    else:
        print('Você perdeu essa.')
    again = input('Quer jogar de novo? ').strip().upper()
    if again == "N":
        break

print(f'Ok, então! \nVocê venceu {countwins} vezes.')
