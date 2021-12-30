
#Variáveis
num = contador = soma = maior = menor = 0 #resumo das variáveis que iniciam todas em 0
resposta = "S" #variável inicial de resposta que inicia em "S"

#Desenvolvimento
while resposta != 'N':
    num = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta != 'S' and resposta != 'N':
      print('Opção inválida. Tente novamente.')
    contador +=1
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior: maior = num
        if num < menor: menor = num

media = soma / contador
print('Você digitou {} números. A média entre eles é {}'.format(contador, media))
print('O maior número digitado é {} e o menor é {}'.format(maior, menor))
