# Programa que determina el mayor de tres número usando if, elif y and
import os;os.system('cls')
print('Determinacion de número mayor.\n')
n1=int(input('Ingrese el primer número: '))
n2=int(input('Ingrese el segundo número: '))
n3=int(input('Ingrese el tercer número: '))
if n1>n2 and n1>n3:
    print(f'\n{n1} es el número mayor.')
if n2>n3 and n2>n1:
    print(f'\n{n2} es el número mayor.')
if n3>n2 and n3>n1:
    print(f'\n{n3} es el número mayor.')
print('\nFin')