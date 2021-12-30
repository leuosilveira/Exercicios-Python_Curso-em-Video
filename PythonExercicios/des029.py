v = int(input('Qual a velocidade? \n'))
multa = (v-80)*7
if v<=80:
    print('Parabéns você estava dentro do limite de velocidade!')
else:
    print('IHH, rapaz! \nVocê exagerou na velocidade e será multado em R$ {:.2f}.\nTenha mais cautela ao dirigir, sua vida pode correr risco!'.format(multa))
