# Clasifica angulos según su amplitud
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo, =360 completo
import os;os.system('cls')
print('Mostrando el tipo de angulo de acuerdo a los grados\n')
angulo=int(input('Ingresa angulo en grados:'))
if angulo>=0 and angulo <=360:
    print('El angulo tiene',angulo,'grados, por lo tanto es un angulo')
    if angulo<90:
        print('agudo')
    elif angulo==90:
        print('recto')
    elif angulo>90 and angulo<180:
        print('obtuso')
    elif angulo==180:
        print('llano')
    elif angulo>180 and angulo<360:
        print('concavo')
    else:
        print('completo')
else:
    print('Angulo fuera de rango')
print('\nProceso terminado')

 
                 
