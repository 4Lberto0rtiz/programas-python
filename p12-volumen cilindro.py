# Programa que calcula el volumen de un cilindro a partir del radio y la altura dados por el usuario
import os;os.system('cls')
import math
print('Calculando volumen de cilindro...\n')
r=float(input('Ingrese el radio del cilindro en metros: '))
a=float(input('Ingrese la altura del cilindro: '))
v=math.pi*(r*r)*a
print(f'\nEl volumen del cilindro es de {v:.2f} metros cúbicos.\n\nProceso terminado.')