# Programa que calcula el promedio de 5 calificaciones ingresadas por el usuario y en base al resultado emite un mensaje 
import os;os.system('cls')
print('Promedio de calificaciones.\nIngresa tus 5 calificaciones separadas por <Enter>')
c1,c2,c3,c4,c5=float(input()), float(input()), float(input()), float(input()), float(input())
p=(c1+c2+c3+c4+c5)/5
if p>0 and p<6:print(f'\nTu promedio es {p}, quedas reprobado.')
elif p>=6 and p<=7:print(f'\nTu promedio es {p}, Pasas de panzazo.')
elif p>7 and p<=8:print(f'\nTu promedio es {p}, muy bien, puedes mejorar.')
elif p>8 and p<=9:print(f'\nTu promedio es {p}, excelente sigue asi.')
elif p>9 and p<=10:print(f'\nTu promedio es {p}, perfecto tu esfuerzo valio la pena.')
else: print('Error: calificaciones fuera de rango')
print('\nFin')