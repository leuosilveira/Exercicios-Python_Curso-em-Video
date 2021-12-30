frase = str(input('Digite sua frase: \n')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palíndromo! \n{} | {}'.format(junto, inverso))
else:
    print('A frase digitada não é um palíndromo.\n{} | {}'.format(junto, inverso))
