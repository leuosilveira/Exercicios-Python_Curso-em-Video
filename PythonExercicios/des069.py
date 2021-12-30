demaior = homens = undertwenty = 0

while True:
    print('-'*30)
    print('NOVO CADASTRO')
    print('-'*30)

    age = int(input('Cadastre uma idade: '))
    if age > 18:
        demaior += 1
    genre = ' '
    while genre not in 'MF':
        genre = input('Cadastre o gênero: [M/F] ').strip().upper()[0]
    if genre == 'M':
        homens += 1
    if age < 20 and genre == 'F':
        undertwenty += 1

    print('-' * 30)
    option = ' '
    while option not in 'SN':
        option = input('Quer continuar? [S/N] ').strip().upper()[0]
    if option == "N":
        break

print(f'{demaior} pessoas possuem mais de 18 anos. \n{homens} pessoas são do gênero masculino. \n{undertwenty} pessoas são mulheres com menos de 20 anos')
