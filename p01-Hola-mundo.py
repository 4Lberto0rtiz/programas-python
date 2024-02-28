# Programa leer datos y enviar un saludo
import os;os.system('cls')
print ('Leyendo datos y enviando un saludo: \n')

nombre= input ('Ingrese nombre: ')
edad=int(input('Ingresa edad: '))
peso=float(input('Ingresa peso: '))

print('Tu nombre es '+nombre+', tu edad es '+str(edad)+', tu peso es '+str(peso))
print('Tu nombre es',nombre,', tu edad es ',edad,', tu peso es ',peso)
print(f'Tu nombre es {nombre}, tu edad es {edad}, tu peso es {peso}')

alerta=peso>80

print(alerta)

print('name_type: ',type(nombre))
print('age_type: ',type(edad))
print('weight_type: ',type(peso))
print('alerta_type: ',type(alerta))
print('Fin')
