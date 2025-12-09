import math 
ang = float(input('Digite um ângulo: '))
ang2 = math.radians(ang)
sen = math.sin(ang2)
cos = math.cos(ang2)
tang = math.tan(ang2)
print('O seno desse ângulo é {}, o seu cosseno é {}, e a sua tangente é {}.'.format(sen, cos, tang))
