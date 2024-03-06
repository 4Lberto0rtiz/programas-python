# Programa que toma tres numeros dados por el usuario y verifica si la suma de los dos primeros es igual al tercero (utilizadno if else)
import os;os.system('cls')
print('Verificacndo suma...\nIngresa tres números enteros separados por un <enter>\n')
n1,n2,n3=int(input()), int(input()), int(input())
if n1+n2==n3:
    print(f'La suma de {n1} y {n2} es igual a {n3}')
else:
    print(f'La suma de {n1} y {n2} es diferente a {n3}')
print('Proceso terminado')