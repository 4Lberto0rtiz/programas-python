# Programa que imprime los numeros impares desde 1 hasta n (n es definido por el usuario) y la suma de los mismos
import os
while(True):
    os.system('cls')
    print('Números nones consecutivos')
    n=int(input('¿Hasta que número? '))
    i=1
    s=1
    while i<=n:
        print(i,end=" ")
        i+=2
        s+=i
    if i==(n+2) or i==(n+1):print(f'\nSumatoria = {s-i}')
    cont=str.upper(input('\n¿Deseas continuar (S/N)?'))
    if cont=='N':break
print('\nFin')
