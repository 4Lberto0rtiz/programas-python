# Programa que imprime numeros de 1 a 200 en incrementos de 10 usando continue
import os;os.system('cls')
print('Multiplos de X de 0 a 200.\n')
m=int(input('Defina X: '))
print('\n')
c=0
while c<=200:
    c=c+1
    if c%m!=0:
        continue
    print(c,end=" ")
print('\n\nFin')