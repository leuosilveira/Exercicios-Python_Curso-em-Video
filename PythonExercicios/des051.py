primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
final = primeiro + (11-1) * razao

for c in range(primeiro, final, razao):
    print('{}'.format(c), end= '» ')
print('Acabou')
