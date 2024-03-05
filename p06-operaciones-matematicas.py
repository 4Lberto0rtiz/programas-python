# Programa que realiza operaciones matematica básicas
import os;os.system('cls')
print('Realizando operaciones matemáticas entre dos numero flotantes...\n')
x=float(input('Ingresa el primer número: '))
y=float(input('Ingresa el segundo número: '))
print('\nMostrando reslutados\n')
suma=x+y
resta=x-y
mult=x*y
div=x/y
residuo=x%y
pot=x**y
divent=x//y
print(f'Suma: {suma}\nResta: {resta}\nMultiplicacion: {mult}\nDivisión: {div}\nResiduo: {residuo}\nPotencia: {pot}\nDivisión entera: {divent}')
