# Programa que cuenta n numreos introducidos por el usuario, cuantos de ellos son negativos, cuantos poositivos, la suma y cuentos fueron 0 (la introduccion de numero se detiene cuando el usuario introduce 999)
import os;os.system('cls')
cuenta=suma=cn=cp=cc=0
print('Conteo de numeros.\n')
while(True  ):
    n=int(input('Número? '))
    if n!=999:
        cuenta=cuenta+1
        suma=suma+n
        if n>0:cp=cp+1
        if n<0:cn=cn+1
        if n==0:cc=cc+1
    else:break
print(f'\nSe introdujeron {cuenta} números')
print(f'La suma es {suma}')
print(f'Positivos: {cp}, negativos: {cn}, ceros: {cc}')
print('\nFin')