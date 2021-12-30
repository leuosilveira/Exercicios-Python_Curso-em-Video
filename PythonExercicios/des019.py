from random import choice
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
lista = [a1,a2,a3,a4]
escolhido = choice(lista)

print('O sorteio ocorrerá entre os alunos: {}'.format(lista))
print('O aluno(a) sorteado foi: {}'.format(escolhido))
