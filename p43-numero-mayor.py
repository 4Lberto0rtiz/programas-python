# Programa que calcula cual es el mayor numero dentro de una serie introducida por el usuario, la serie se ingresa via teclado hasta que se introduce el 0
import os
import math
cont='SI'
while cont=='SI':
    os.system('cls')
    print('CALCULANDO NÚMERO MAYOR DENTRO DE LA SERIE:\n(Ingrese "0" para terminar)\n')
    nm=n=int(input('Ingresar número: '))
    c=0
    while n!=0:
        n=int(input('Ingresar número: '))
        c+=1
        if n>=nm and n!=0:
            nm=n
    print(f'\nSe ingresaron {c} números, de los cuales {nm} es el mayor.')
    cont=str.upper(input('\n¿Deseas continuar (SI/NO)? '))
    while cont!='NO' and cont!='SI':
        cont=str.upper(input('\nRespuesta no válida\n¿Deseas continuar (SI/NO)? '))
print('\nFin')