h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
a = l * h
l = a / 2
print('Para uma parede que mede {:.2f}m² de área, precisaremos de {:.2f} litros de tinta'.format(a,l))
