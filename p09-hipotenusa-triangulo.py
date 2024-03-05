# Programa que calcula la hipotenusa de un triangulo rectangulo, usando los catetos dados por el usuario
import os
os.system('cls')
import math
print('Calculando la hipotenusa de un triangulo...\nIngrese las medidas de los lados del triangulo separados por espacios:')
co,ca=input().split()
co,ca=int(co),int(ca)
hip=math.sqrt(co*co+ca*ca)
print(f'Un triangulo rectangulo cuyos lados miden {co} y {ca} tiene una hipotenusa de:{hip:.2f}\n\nProceso terminado')