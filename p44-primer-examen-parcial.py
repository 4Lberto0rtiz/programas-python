# Programa que lleva el control de inscripciones a un evento académico, en el cual el usuario indica el tipo de usuario y el tipo de paquete que desea y se aplican los descuentos correspondientes, se calcula un subtotal por cada iteracion y al final se calcula el total de ventas.
import os;os.system('cls')
r='SI'
mf=0 #mf=monto final 
while r=='SI':
    print('\n\nUniversidad Patito SA de CV\nSistema de inscripción al Congreso de Sistemas\n')
    u=str.upper(input('Tipo de usuario ([1]Alumno $ 100, [2]Trabajador $ 200, [3]Docente $ 500): '))
    while u!='1' and u!='2' and u!='3':
        u=str(input('¡¡¡Respuesta no válida!!!\nTipo de usuario ([1]Alumno $ 100, [2]Trabajador $ 200, [3]Docente $ 500): '))
    t=str.upper(input('Tipo de paquete ([1]Solo conferencias $ 600, [2]Con eventos sociales $ 800, [3]Con kit de acceso $ 900): '))
    while t!='1' and t!='2' and t!='3':
        t=str(input('¡¡¡Respuesta no válida!!!\nTipo de paquete ([1]Solo conferencias $ 600, [2]Con eventos sociales $ 800, [3]Con kit de acceso $ 900): '))
    c=int(input('Cantidad: '))
    pu=pp=d=st=Total=desc=0
    tu=tp=td='0 %'
    if u=='1':pu=100;tu='Alumno'
    elif u=='2':pu=200;tu='Trabajador'
    elif u=='3':pu=500;tu='Docente'
    if t=='1':tp='Solo conferencias';pp=600
    elif t=='2':pp=800;tp='Con eventos sociales'
    elif t=='3':pp=900;tp='Con kit de acceso'
    st=c*(pu+pp)
    if st>=5000 and tu=='Alumno':d=0.2;td='20 %'
    elif st>=5000 and tu=='Trabajador':d=0.1;td='10 %'
    elif st>=5000 and tu=='Docente':d=0.05;td='5 %'
    desc=st*d
    Total=st-desc
    print(f'Tu pedido fue: {c}, Tipo de usuario: {tu}, Tipo de paquete: {tp}\nSubtotal: $ {st} con un descuento de $ {desc} ({td}) y un total de $ {Total}')
    mf+=Total
    r=str.upper(input('\n¿Deseas continuar (SI/NO)? '))
    while r!='NO' and r!='SI':
        r=str.upper(input('\n¡¡¡Respuesta no válida!!!\n¿Deseas continuar (SI/NO)? '))
print(f'\nImporte total de la venta: $ {mf}')
print('\nProceso terminado...')