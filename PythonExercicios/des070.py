#Calculadora de compras

print('-'*30)
print('LOJA SUPERLEO')
print('-'*30)

totalcompra = acimademil = valormaisbarato = cont = 0
produtobarato = ' '

while True:
    produto = input('Nome do produto: ').strip().upper()
    preco = float(input('Preço do produto: '))
    totalcompra += preco
    if preco > 1000:
        acimademil += 1
    cont += 1
    if cont == 1 or preco < valormaisbarato:
        valormaisbarato = preco
        produtobarato = produto
    opcao = ' '
    opcao = input('Quer continuar? [S/N]').strip().upper()[0]
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N]').strip().upper()[0]

    if opcao == 'N':
        break

print('{:-^40}'.format('OBRIGADO PELAS COMPRAS, VOLTE SEMPRE!'))

print(f'O total gasto foi de R$ {totalcompra:.2f} \nCom {acimademil} produto(s) acima de R$ 1.000 \nSendo {produtobarato} o produto mais barato')
