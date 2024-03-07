# Programa que imprime una tabla de conversion Peso a Dollar usando while
import os;os.system('cls')
while(True):
    print('\nTabla de conversion de peso a dolar...\n')
    tc = 17.00
    vi = float(input("Valor inicial: "))
    vf = float(input("Valor final : "))
    c = vi
    print('\nPeso\tDolar')
    print('-'*15)
    while c<=vf:
        print(f'{c}\t{c/tc:.2f}')
        c=c+1
    print('-'*15)
    op=str.upper(input('\nDesas ontinuar(S/N)? '))
    if op=='N':break
print('\nFin')