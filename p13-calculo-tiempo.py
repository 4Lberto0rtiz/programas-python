# Programa que convierte horas a días minutos y segundos
import os;os.system('cls')
print('Conversor de horas a días, minutos y segundos\n')
h=int(input('Ingrese la cantidad de horas: '))
d,m,s=int(h/24),h*60,h*3600
print(f'\n{h} hora(s) equivalen a {d} día(s), {m} minutos y {s} segundos.\n\nProceso terminado.')