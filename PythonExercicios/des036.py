casa = float(input('Qual o valor da casa que você deseja comprar?\n'))
salario = float(input('Qual sua renda mensal? \n'))
anos = int(input('Em quantos anos você pretende quitar o empréstimo? \n'))
qnt_prestacao = anos * 12
vlr_prestacao = casa / qnt_prestacao
margem = salario * 0.30
utilizacao_margem = vlr_prestacao / margem

if utilizacao_margem > 0.80 and utilizacao_margem <= 1:
    print('Para pagar uma casa de R${:.2f}, em {} anos, a prestação será de R${:.2f} em {} vezes. '.format(casa,anos,vlr_prestacao,qnt_prestacao))
    print('Parabéns o empréstimo será \033[1:32mCONCEDIDO!')
    print('\033[33mMas tome cuidado, pois estará comprimetendo quase 30% de sua renda!')
elif vlr_prestacao <= margem:
    print('Para pagar uma casa de R${:.2f}, em {} anos, a prestação será de R${:.2f} em {} vezes. '
          '\nParabéns o empréstimo será \033[1:32mCONCEDIDO!'.format(casa,anos,vlr_prestacao,qnt_prestacao))
else:
    print('Para uma casa de R${:.2f}, em {} anos, a prestação será de R${:.2f} em {} vezes.'
          '\nSinto muito, mas neste caso o empréstimo foi \033[1:31mNEGADO.')
