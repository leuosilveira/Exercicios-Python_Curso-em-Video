nome = str(input('Qual teu nome?\n'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'brancopreto':'\033[7m'}
print('Muito prazer em te conhecer {}{}{}'.format(cores['brancopreto'],nome,cores['limpa']))
