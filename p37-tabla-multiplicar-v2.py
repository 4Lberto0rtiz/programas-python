# Programa que imprime las tablas de multiplicar determinadas por el usuario
import os
while(True):
    os.system('cls')
    print('Tablas de multiplicar...')
    h=int(input('¿Hasta que tabla quieres? '))
    d=int(input('¿Hasta que número desas las tablas? '))
    n=1
    while n<=h:
        print(f'\nTabla del {n}')
        t=1
        while t<=d:
            print(f'{n} x {t} = {n*t}')    
            t+=1 
        n+=1
    op=str.upper(input('\n¿Desas continuar (S/N)? '))
    if op=='N':break
print('\nProceso terminado')