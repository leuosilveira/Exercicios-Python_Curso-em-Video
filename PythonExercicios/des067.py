while True:
    print('-' * 50)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*50)
    if num < 0:
        break
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
print('Programa finalizado. \nObrigado e volte sempre!')