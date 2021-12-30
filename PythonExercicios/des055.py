maximo = 0
minimo = 500
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > maximo:
        maximo = peso
    if peso < minimo:
        minimo = peso
print('O maior peso digitado foi {}Kg, e o menor peso foi {}Kg.'.format(maximo,minimo))
