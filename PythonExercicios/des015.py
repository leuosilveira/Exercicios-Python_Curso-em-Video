km = float(0.15)
dist = float(input('Quantos KM rodados? '))
diaria = int(60)
dias = int(input('Quantos dias alugados? '))
total = km * dist + diaria * dias
print('O total a pagar é R$ {:.2f}'. format(total))
