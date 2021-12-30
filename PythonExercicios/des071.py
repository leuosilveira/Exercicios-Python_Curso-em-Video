print('='*40)
print("Leo's Bank")
print('='*40)
print('Cédulas disponíveis: 50, 20, 10 e 1')
saque = int(input('Digite o valor que pretende sacar: R$'))
cedula = 50
totalcedulas = 0

while True:
    if saque >= cedula:
        saque -= cedula
        totalcedulas += 1
    else:
        if totalcedulas != 0:
            print(f'Total de {totalcedulas} cédula(s) de R$ {cedula:.2f}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        totalcedulas = 0

        if saque == 0:
            break

