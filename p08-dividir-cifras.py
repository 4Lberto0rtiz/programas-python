# programa que divide un numero entero de 3 cifras en sus digitos individuales (unidades, decenas y centenas)
import os;os.system('cls')
print('Separando numero entero por cifras...\n')
n=int(input('Ingrese número entero de tres cifras: '))
uni=n%10 
n//=10  
dec=n%10
n//=10
cen=n%10
print(f'Centenas: {cen}\nDecenas: {dec}\nUnidades: {uni}')