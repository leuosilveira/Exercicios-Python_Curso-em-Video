num = soma = c = 0
num = int(input('Digite um número a sua escolha [999 para parar]: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('Digite um número a sua escolha [999 para parar]: '))
print('Foram digitados {} números e a soma entre eles é {}'.format(c, soma))
