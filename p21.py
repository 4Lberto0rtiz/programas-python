# Aceptar o rechazar estuidante con base en su edad y dos calificaciones
import os;os.system('cls')
print('Universidad Patito SA de CV')
print('Validación de inscripción')

nombre=input('Ingresa nombre:')
Edad=int(input('Ingresa tu edad:'))

if Edad<18:
    print('Los sentimos,',nombre,'solo aceptamos estudiantes mayores de Edad')
else:
    print('Ingresa dos calificaciones separadas por un <Enter>')
    c1,c2=int(input()),int(input())
    if c1<8 or c2<8:
        print('Solo aceptamos estudiantes de ocho')
    else:
        print(nombre,', Bienvenido! cumpliste son los requisitos de edad y calificaciones')
print('\nProceso terminado')


