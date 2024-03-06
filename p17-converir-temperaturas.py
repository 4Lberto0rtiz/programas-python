# Programa que convierte temperaturas Celsius-Farenheit utilizando if
print('Conversión de temperaturas F<->C')
opcion = str.upper(input('[C]elsius\n[F]ahrenheit\nElije ') )
if opcion == 'C':
    print('\nConviritiendo a Farenheit...')
    temp = float(input('Ingrese la temperatura en grados Celsius: '))
    f = ( temp * 9 / 5 ) + 32
    print(f'\n{temp}°c, equivalen a {f}°f.') 
else :
    print('\nConviritiendo a Celsius...')
    temp = float(input('Ingrese temperatura en grados Farenheit: '))
    c = (temp - 32) * 5 / 9
    print(f'\n{temp}°F equivalen a {c}°C.') 
print('\nFin')