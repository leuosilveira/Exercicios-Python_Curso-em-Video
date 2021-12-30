from datetime import date
genero = str(input('Qual seu gênero? \n[f] - Feminino\n[m] - Masculino\n'))
if genero == 'f':
    print('Você não possui obrigatoriedade de se alistar.')
elif genero == 'm':
    birth = int(input('Em que ano você nasceu?\n'))
    age = date.today().year - birth
    alistamento = birth + 18
    diferenca = date.today().year - alistamento

    if age < 18:
        print('Você possui {} anos de idade.'.format(age))
        print('Falta {} anos para o seu alistamento.'.format(diferenca*-1))
        print('\033[1;33mVocê deverá se alistar somente em {}.'.format(alistamento))
    elif age == 18:
        print('Você possui {} anos de idade'.format(age))
        print('Você tem que se alistar \033[1;33mIMEDIATAMENTE!')
    else:
        print('Você possui {} anos de idade.'.format(age))
        print('\033[1;33mVocê já deveria ter se alistado há {} anos.\033[m'.format(diferenca))
        print('Seu alistamento foi em {}'.format(alistamento))
else:
    print('Opção inválida. \nPor favor escolha entre f ou m.\nTente novamente.')