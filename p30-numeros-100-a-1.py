# Programa que imprime numeros de n a 1 en decrementos de i
import os;os.system('cls')
print('Numeros regresivos.\n')
n=int(input('¿Desde que número? '))
i=int(input('¿De cuanto en cuanto? '))
while n>=1:
    print (n, end=" ")
    n=n-i
print('\n\nFin')