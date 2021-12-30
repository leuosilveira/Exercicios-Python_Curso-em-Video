altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura**2
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Seu IMC indica: ABAIXO DO PESO.')
elif imc < 25:
    print('Seu IMC indica: PESO IDEAL.')
elif imc < 30:
    print('Seu IMC indica: SOBRE PESO.')
elif imc < 40:
    print('Seu IMC indica: OBESIDADE.')
else:
    print('Seu IMC indica: OBESIDADE MÓBIDA.')
