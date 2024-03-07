# Programa que imprime los numeros pares de manera descendente desde 100 hasta n (n es definido por el usuario) y la suma de los mismos
import os
while(True):
    os.system('cls')
    print('Números pares descendentes')
    n=int(input('¿Hasta que número? '))
    i=100
    s=100
    while i>=n:
        print(i,end=" ")
        i-=2
        s+=i
    if i==(n-1) or i==(n-2):print(f'\nSumatoria = {s-i}')
    cont=str.upper(input('\n¿Deseas continuar (S/N)?'))
    if cont=='N':break
print('\nFin')