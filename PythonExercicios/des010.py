r = float(input('Quantos reais você tem na carteira? '))
d = r / 5.68
e = r / 6.86
ether = r / 8614.43
print('Com R${:.2f}, você poderia comprar US${:.2f}, £${:.2f} ou {:.4f} Ether'.format(r,d,e,ether))
