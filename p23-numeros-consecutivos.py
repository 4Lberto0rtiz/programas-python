# programa que, usando if y and, determina si tres numeros dados por el usuario son consecutivos
import os;os.system('cls')
print('Verificación de números consecutivos\nIngrese tres numeros enteros separados por <Enter>')
n1,n2,n3=int(input()), int(input()), int(input())
if n3==n2+1 and n2==n1+1:
    print(f'\nLos números {n1}, {n2} y {n3} son consecutivos.')
elif n2==n3+1 and n3==n1+1:
    print(f'\nLos números {n1}, {n2} y {n3} son consecutivos, pero no en ese orden.')
elif n3==n1+1 and n1==n2+1:
    print(f'\nLos números {n1}, {n2} y {n3} son consecutivos, pero no en ese orden.')
elif n2==n1+1 and n1==n3+1:
    print(f'\nLos números {n1}, {n2} y {n3} son consecutivos, pero no en ese orden.')
elif n1==n3+1 and n3==n2+1:
    print(f'\nLos números {n1}, {n2} y {n3} son consecutivos, pero no en ese orden.')
elif n1==n2+1 and n2==n3+1:
    print(f'\nLos números {n1}, {n2} y {n3} son consecutivos, pero no en ese orden.')
else:
    print('Los números ingresados no son consecutivos')
print('\nFin')