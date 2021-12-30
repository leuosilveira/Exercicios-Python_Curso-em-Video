print('Olá!\nvou te ajudar a calcular o valor do aumento que você receberá.')
sal = float(input('Qual o seu salário atual? \n R$'))
if sal > 1250.00:
    print('Seu salário final será de R${:.2f}, pois seu aumento foi de 10%.'.format(sal+sal*0.10))
else:
    print('Seu salário final será de R${:.2f}, pois seu aumento foi de 15%.'.format(sal+sal*0.15))
