num = cont = soma = 0
while True:
    num = int(input("Digite um número ou 999 para parar: "))
    if num == 999:
        break
    else:
        soma += num
        cont += 1

print(f'Foram digirados {cont} números e a soma entre eles é {soma}.')

