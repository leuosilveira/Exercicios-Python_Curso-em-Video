nome = input('Qual o seu nome?\n').strip()
first_name = nome.split()
print('Analisando seu nome... ')
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(len(first_name[0])))
