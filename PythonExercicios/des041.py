from datetime import date

birth = int(input('Digite o ano de nascimento do atleta: '))
age = date.today().year - birth
print('O atleta tem {} anos.'.format(age))

if age <= 9:
    print('Classificação: MIRIM.')
elif age <= 14:
    print('Classificação: INFANTIL.')
elif age <= 19:
    print('Classificação: JÚNIOR.')
elif age <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER')
