print('Olá! \nTe ajudarei a comparar dois número e verificar qual é o maior. ')
print('- - ' * 20)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O PRIMEIRO valor é o maior.')
elif num2 > num1:
    print('O SEGUNDO valor é o maior.')
else:
    print('Não existe valor maior, os dois valores são iguais.')
