# Programa que determina si un numero dado por el uysuario es negativo, positivo o es igual a cero
import os;os.system('cls')
print('Verificación numerica\n')
n=int(input('Ingresa un número: '))
if n<0:
    print(f'\n{n} es negativo')
if n>0:
    print(f'\n{n} es positivo')
if n==0:
    print(f'\nEl numero es igual a cero')
print('\nProceso terminado.')