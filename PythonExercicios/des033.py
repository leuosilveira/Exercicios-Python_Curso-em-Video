num1 = int(input('Escreva o primeiro número: \n'))
num2 = int(input('Escreva o segundo número: \n'))
num3 = int(input('Escreva o terceiro número: \n'))

#Validação do maior

if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

#Validação do menor
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitato é {}'.format(menor))
