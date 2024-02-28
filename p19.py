# Verificar si la suma de dos numeros es igual a un tercero
print('verificando si la suma de dos numeros es igualk a un tercero')
print('Dame tres números separados por espacios')

n1, n2, n3 =input().split()
n1, n2, n3 =int(n1), int(n2), int(n3)

if n1+n2==n3:
    print(f"Caso 1: {n1}+{n2}={n3}")
elif n1+n3==n2:
    print(f"Caso 2: {n1}+{n3}={n2}")
elif n2+n3==n1:
    print(f"Caso 3: {n2}+{n3}={n1}")
elif n1==n2==n3:
    print(f"Caso 4: {n1}={n2}={n3}")
else:
    print('Caso 5: No son iguales y no suman')

print('\n Proceso terminado')