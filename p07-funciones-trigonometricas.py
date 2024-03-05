# Programa que calcula las funciones trigonometricas partiendo de un angulo dado por el usuario
import math
import os
os.system('cls')
print('Calculo de funciones trigonometricas\n')
angulo=float(input('ingresa el angulo en radianes: '))
ang=math.degrees(angulo)
sen=math.sin(angulo)
cos=math.cos(angulo)
tan=math.tan(angulo)
print(f'\nResumen de funciones trigonometricas\n\nSeno: {sen}\nCoseno: {cos}\nTangente: {tan}\n\nEl angulo de {angulo} radianes equivale a {ang:.2f} grados')