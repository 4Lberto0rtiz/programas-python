# Programa que calcula de paga de un trabajador considerando las horas extras
import os;os.system('cls')
print('Calculando la paga de horas extra de un trabajador...\n')
nombre=input('Ingresa tu nombre:')
horas=int(input('Ingresa las horas trabajadas:'))
paga=float(input('Ingresa la paga por hora: '))
extra=pagaextra=total=0 #se inicializan las variables ya que al encontrarse despues de un condicional pueden no definirse y generan error
if horas<=40:
    print(())
else:
    extra=horas-40
print(f'\nEl trabajador {nombre}\nTrabajo: {horas-extra} horas\nCon una paga de {paga} pesos por hora\nTrabajo {extra} horas extra pagadas al doble\nPago normal: {(horas-extra)*paga}\nPago horas extra: {paga*extra*2}\nPago total: {(paga*extra*2)+((horas-extra)*paga)}')
print('\nFin')
