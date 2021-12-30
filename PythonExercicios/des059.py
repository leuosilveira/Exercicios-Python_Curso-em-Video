from time import sleep

#primeira solicitação de números
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#desenvolvimento
soma = num1 + num2
multiplicacao = num1 * num2
maior = num1
if num2 > maior:
    maior = num2
escolha = 0


while escolha != 5:
    print('- - ' * 20)
    print('[1] Somar\n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Finalizar Programa')
    escolha = int(input('Qual sua escolha? '))

    if escolha == 1:
        print('A soma dos entre {} e {} é {}.'.format(num1, num2, soma))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é {}.'.format(num1, num2, multiplicacao))
    elif escolha == 3:
        print('Entre {} e {}, o maior número é {}.'.format(num1, num2, maior))
    elif escolha == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        soma = num1 + num2
        multiplicacao = num1 * num2
        maior = num1
        if num2 > maior:
            maior = num2
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! \nTente novamente.')
    sleep(1.5)
print('Ok')