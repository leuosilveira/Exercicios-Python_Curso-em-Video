p = float(input('Qual o preço original? R$'))
d = p - (p * 0.05 - p)
j = p + (p *0.10)
print('O valor final, se pagar a vista será R${:.2f}, mas se você parcelar será R${:.2f}'.format(d,j))

