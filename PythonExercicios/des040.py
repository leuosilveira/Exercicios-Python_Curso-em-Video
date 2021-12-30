print('Olá!\nVou te ajudar a descobrir se você foi Aprovado, Reprovado ou está em Recuperação.')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('\033[1;32mParabéns! \nSua média é {:.1f} e você foi APROVADO!'.format(media))
elif media < 5:
    print('\033[1;31mSinto muito. \nSua média final é {:.1f}. \nVocê não atingiu uma média satisfatória e foi REPROVADO.'.format(media))
else:
    print('\033[1;33mAtenção! \nSua média final é {:.1f}. \nVocê não atingiu uma média satisfatória, mas está perto, portanto ficará em RECUPERAÇÃO.'.format(media))
