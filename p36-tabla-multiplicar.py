# Programa que imprime una tabla de multiplicar dada por el usuario
import os
while(True):
    os.system('cls')
    print('Construyendo tabla de multiplicar...\n')
    t = int(input('Que tabla quieres? '))
    n = int(input('Hasta donde la quieres? '))
    c = 1
    while( c <= n):
        print(f'{t} x {c} = {t*c}')
        c+=1
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':break
print("\nProceso terminado.")