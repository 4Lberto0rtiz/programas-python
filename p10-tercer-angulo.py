# Programa que calcula el angulo interno de un triangulo a partir de las medidas de dos angulos dados por el usuario
import os;os.system('cls')
print('Calculando tercer angulo...\nPor favor ingrese el valor de los angulos 1 y 2, separado por espacios:')
a1,a2=input().split()
a1,a2=int(a1),int(a2)
a3=180-(a2+a2)
print(f'El triangulo con angulos internos de {a1}° y {a2}°, tiene un tercer angulo de {a3}°\n\nProceso terminado.')