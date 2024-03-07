# Programa que imprime la cuenta y suma de los numeros introducidos por el usuario hasta que la suma llega a 200
import os
cont='SI'
while cont=='SI':
    os.system('cls')
    print('Sumando hasta 200\n')
    s=c=0
    while s<200:
        n=float(input('Ingresar número: '))
        s+=n
        c+=1 
    print(f'\nSe ingresaron {c} números\nSumatoria = {s}')
    cont=str.upper(input('\n¿Deseas continuar (SI/NO)? '))
    while cont!='NO' and cont!='SI':
        cont=str.upper(input('\nRespuesta no válida\n¿Deseas continuar (SI/NO)? '))
print('\nFin')