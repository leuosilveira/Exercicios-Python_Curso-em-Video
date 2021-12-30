print('{:=^40}'.format(" SILVEIRINHA'S STORE "))
valor = float(input('Valor das compras: '))
print('''FORMAS DE PAGAMENTO:
[1] A VISTA DINHEIRO/CHEQUE
[2] A VISTA CARTÃO
[3] 2x NO CARTÃO
[4] 3x OU MAIS NO CARTÃO''')
pgto = int(input('Escolha a forma de pagamento: '))
if pgto == 1:
    print('Sua compra de R${:.2f}, recebeu um desconto de 10%. \nValor final é R${:.2f}.'.format(valor,valor-(valor*0.10)))
elif pgto == 2:
    print('Sua compra de R${:.2f}, recebeu um desconto de 5%. \nValor final é R${:.2f}.'.format(valor, valor - (valor * 0.05)))
elif pgto == 3:
    print('Sua compra de R${:.2f} será dividida em duas parcelas de {:.2f}.'.format(valor,valor/2))
elif pgto == 4:
    print('Sua compra de R${:.2f}, receberá um acrescimo de 20% de juros. \nValor final será R${:.2f}.'.format(valor,valor+(valor*0.10)))
    parcelas = int(input('Em quantas parcelas? '))
    print('Suas parcelas ficarão de R${:.2f}'.format((valor+(valor*0.10)) / parcelas))
else:
    print("Por favor, escolha uma opção válida entre os números 1, 2, 3 e 4.")
