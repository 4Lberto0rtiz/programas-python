# Verificar si la suma de dos numeros es igual a un tercero
import os;os.system('cls')
print('Verificando si la suma de dos numeros es igual a un tercero')
print('Dame tres números separados por espacios')

n1, n2, n3 =input().split()
n1, n2, n3 =int(n1), int(n2), int(n3)

if n1+n2==n3:
    print(f"\nCaso 1: {n1}+{n2}={n3}")
elif n1+n3==n2:
    print(f"\nCaso 2: {n1}+{n3}={n2}")
elif n2+n3==n1:
    print(f"\nCaso 3: {n2}+{n3}={n1}")
elif n1==n2==n3:
    print(f"\nCaso 4: {n1}={n2}={n3}")
else:
    print('\nCaso 5: No son iguales y no suman')

print('\nProceso terminado')