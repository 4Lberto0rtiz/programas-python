# Programa que determina si un aspirante es aceptado en la universidad Kitti kat, donde solo aceptan mujeres mayores de 21 con promedio entre 8 y 9.5
import os;os.system('cls')
print('Proceso de ingreso a la Universidad Kitty Kat SA\n')
nombre=str(input('Nombre: '))
s=str.upper(input('sexo(H/M): '))
if s=='H':print('\nLos sentimos solo aceptamos mujeres')
elif s=='M':
    edad=int(input('Edad: '))
    if edad<21:print('\nNo tienes la edad suficiente, debes tener 21 años cumplidos')
    elif edad>=21:
        c1=float(input('Calificacion 1: '))
        c2=float(input('Calificacion 2: '))
        c3=float(input('Calificacion 3: '))
        p=(c1+c2+c3)/3
        if p<8:print(f'\nTu promedio es de {p:.2f}, no es suficiente, no aceptamos promedios por debajo de 8.')
        elif p>9.5:print(f'\nTu promedio es de {p}, no aceptamos promedios por arriba de 9.5.')
        else:print('\nCumpliste con los requisitos\n¡Bienvenida ala universidad Kitty Kat SA!')
else:print('\nSexo no reconocible')
print('\nFin')