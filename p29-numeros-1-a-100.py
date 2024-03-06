# Programa que imprime numeros de 1 a n en incrementos de i
import os;os.system('cls')
print('Numeros consecutivos.\n')
n=int(input('¿Hasta que número? '))
i=int(input('¿De cuanto en cuanto? '))
c=0
while c<=n:
    print (c, end=" ")
    c=c+i
print('\n\nFin')