cidade = str(input('Digite o nome de sua cidade: \n').strip().upper())
cidade01 = cidade.split()
print('O nome de sua cidade começa com a palavra Santo: {}'.format('SANTO' in cidade01[0]))
