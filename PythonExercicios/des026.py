frase = str(input('Digite uma frase: \n')).strip().upper()
print('A letra a aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra a aparece na posição {}.'.format(frase.find('A')+1))
print('A última letra a aparece na posição {}.'.format(frase.rfind('A')+1))
