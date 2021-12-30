num = int(input('Digite um número inteiro: \n'))
print('Escolha uma das bases a seguir para conversão:')
print('[1] para converter em BINÁRIO')
print('[2] para coverter em OCTAL')
print('[3] para converter em HEXADECIMAL')
opcao = int(input('Por favor, escolha uma opção digitando 1, 2 ou 3: \n'))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Por favor, escolha uma opção entre 1 a 3.')
