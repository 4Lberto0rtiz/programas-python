# Programa que imprime numeros de 1 a 200 hasta alcanzar la suma de 100
import os;os.system('cls')
print('Suma de numeros consecutivos (ejemplo de break)\n')
c=0
s=0
while c<=200:
    c+=1
    s+=c
    print(c,end=" ")
    if s>=3000:
        break
print(f'\n\nHemos alcanzado la meta {s}, sumando {c} numeros') 