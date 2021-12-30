genero = str(input('Qual seu gênero? \n[M/F]\n')).strip().upper()
while genero != 'M' and genero != 'F':
    print('Opção inválida, por favor digite M para Masculino ou F para Feminino. \nTente novamente:')
    genero = str(input('Qual seu gênero? \n[M/F]\n')).strip().upper()
print('Thank you!')
