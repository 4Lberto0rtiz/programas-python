# Progarma que calcula el promedio de 3 calificaciones
import os;os.system('cls')
print('Calculando el promedio de tres calificaciones...')
print('dame tres calificaciones separadas por espacios') 
c1,c2,c3=input().split( )
c1,c2,c3=int(c1),int(c2),int(c3)
promedio=(c1+c2+c3)/3
print(f'el promedio de {c1}, {c2}, {c3} es: {promedio:.2f}')