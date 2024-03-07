# Programa que demuestra la conjetura de collatz
import os;os.system('cls')
while(True):
    print('\nDemostrando la conjetura de collatz...\n')
    n=int(input('Ingresa un numero entero positivo(puede ser tan grande como quieras): '))
    while n!=1:
        print(n,end=" ")
        if n%2==0:
            n//=2
        else:
            n=n*3+1
    print(n)
    op=str.upper(input('¿Desea continuar (S/N)? '))
    if op=='N':break
print('\nFin')