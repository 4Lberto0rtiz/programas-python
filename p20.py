# Calcula los valores de la segunda ley de Newton
import os;os.system('cls')
print('Calculando los valores de la segunda ley de Newton \n')
print('[f]=m*a')
print('[m]=f/a')
print('[a]=f/m')
op=input('elige una opcion').lower()

if op=='f':
    print('Calculando fuerza...')
    m=float(input('Ingresa masa:'))
    a=float(input('Ingresa aceleracion:'))
    f=m*a
    print('la fuerza es',f)
elif op=='m':
    print('Calculando masa...')
    f=float(input('Ingresa fuerza:'))
    a=float(input('Ingresa aceleracion:'))
    m=f/a
    print('la masa es',m)
elif op=='a':
    print('Calculando aceleracion...')
    m=float(input('Ingresa masa:'))
    f=float(input('Ingresa feurza:'))
    a=f*m
    print('la aceleracion es',f)
else:
    print('Opcion incorrecta')
print('\n Proceso terminado')