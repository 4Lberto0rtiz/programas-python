# Calculo de paga e impuestos de trabajador
import os;os.system('cls')
print('Calculando la paga de un trabajador')
nombre=input('dame tu nombre:')
horas=int(input('Dame las horas trabajadas:'))
paga=float(input('dame la paga por hora: '))
tasa=0.3
pagabruta=horas*paga
impuesto=pagabruta*tasa
paganeta=pagabruta-impuesto
print('\nResumen de pagos:\n')
print(f'El trabajador {nombre} trabajo un total de {horas} horas, con una paga de {paga} pesos y una tasa de impuestos de {tasa}%')
print(f'Paga bruta :{pagabruta:.2f}')
print(f'Impuesto   :{impuesto:.2f}')
print(f'Paga neta  :{paganeta:.2f}')
print('end')