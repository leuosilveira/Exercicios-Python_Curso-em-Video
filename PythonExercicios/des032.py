from datetime import date
print('Olá!\nVou te ajudar a identificar se um determinado ano é bissexto.')
ano = int(input('Escreva um ano para analisarmos: \n(Ou coloque o número zero para analisar o ano atual)\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano de {} é um ano bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano bissexto!.'.format(ano))
