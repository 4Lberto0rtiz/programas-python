# Este programa calcula el area de un circulo
import math
print('Calculando el área de un curculo')
radio=float(input('ingrese el radio:'))
#area=3.1416*radio*radio
area = math.pi * math.pow(radio,2)

print(f'el circulo de radio {radio}, tiene un área de {area:.2f}')
