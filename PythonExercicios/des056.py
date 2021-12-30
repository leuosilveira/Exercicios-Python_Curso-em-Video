media_idade = 0
olderman = 0
name_olderman = str
youngers = 0

for p in range(1,5):
    print('Digite os dados da {}ª pessoa: '.format(p))
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    gender = str(input('Sexo: '))
    media_idade += age
    if gender == 'm':
        if age > olderman:
            olderman = age
            name_olderman = name
    if gender == 'f':
        if age < 20:
            youngers += 1
print('A média das idades dos participantes da pesquisa é: {:.2f}'.format(media_idade/4))
print('O nome do homem mais velho é {} e ele tem {} anos.' .format(name_olderman, olderman))
print('A quantidade de mulheres com menos de 20 anos na pesquisa é {}.' .format(youngers))
