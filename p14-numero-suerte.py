# Programa que genera un número de la suerte sumando las cifras individuales del año de nacimiento del usuario)
import os;os.system('cls')
print('Calculando tu número de la suerte...\n')
n=int(input('¿En que año naciste? '))
uni=n%10 
n//=10  
dec=n%10
n//=10
cen=n%10
n//=10
mil=n%10
ns=uni+dec+cen+mil
print(f'\n¡Tu número de la suerte es el {ns}!')