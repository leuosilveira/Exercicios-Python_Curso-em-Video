from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(1,8):
    person = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if (ano - person) >= 21:
        maior += 1
    else:
        menor += 1

print('Das sete pessoas cujas você digitou o ano e nascimento, {} já alcançaram a maioridade e {} ainda não.'.format(maior,menor))
