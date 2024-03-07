# Programa que imprime una tabla de conversion de celsius a farenheit en un rango dado por el usuario
import os
cont='SI'
while cont=='SI':
    os.system('cls')
    print('Tabla de conversión C-F.\n\nIngrese el rango:\n')
    i=int(input('Limite infeior: '))
    s=int(input('Limite superior: '))
    print(f'\nTabla de conversion C - F')
    print('-'*13)
    while i<=s:
        print(f'{i}°C = {(i*9/5)+32}°F')
        i+=1 
    print('-'*13)
    cont=str.upper(input('\n¿Deseas continuar (SI/NO)? '))
    while cont!='NO' and cont!='SI':
        cont=str.upper(input('\nRespuesta no válida\n¿Deseas continuar (SI/NO)? '))
print('\nFin')