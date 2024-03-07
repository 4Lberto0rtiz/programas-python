# Programa que lee una serie de numeros introducidos por el usuario hasta que este intrdusca 0, posteiormente imprime la sumatoria y el promedio de los mismos
import os
while(True):
    os.system('cls')
    s=c=0
    print('SUMA Y PROMEDIO')
    while(True):
        n=int(input('Ingresar número: '))
        if n!=0:
            s+=n
            c+=1
        else:break
    print(f'\nSe introdujeron {c} números\nSumatoria = {s}\nPromedio = {s/c}')
    cont=str.upper(input('\n¿Deseas continuar (S/N)?'))
    if cont=='N':break
print('\nFin')