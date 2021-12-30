print('Olá! Vou te ajudar a avaliar o tipo de algo que você digitar.')
a = input('Por favor, digite algo: ')
print('o tipo primitivo deste valor é {}. Ele só tem Espaços? {}. Ele é um Número? {}. Ele está em maúsculo? {}. Ele está em minúsculo? {}'.format(type(a),a.isspace(),a.isnumeric(),a.isupper(),a.islower()))
