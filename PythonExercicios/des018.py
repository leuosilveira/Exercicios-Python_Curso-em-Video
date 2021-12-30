from math import radians,sin,cos,tan
ang = float(input('Digite o valor do ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Para um ângulo de {}°, segue os valores: \nsen: {:.4f} \ncos: {:.4f} \ntan: {:.4f}'.format(ang,sen,cos,tan))
