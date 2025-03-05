import time
import os

def temporizador(tiempo):
    time.sleep(tiempo)
    print('El Tiempo ha finalizado ')
    os.system("afplay /System/Library/Sounds/Ping.aiff")
    
def pomodoro():
    print('Pomodoro')
    activo = float(input('Tiempo de Actividad en minutos: ')) * 60
    descanso = float(input('Tiempo de descanso en minutos: ')) * 60
    repeticiones = int(input('Cantidad de repeticiones: '))
    for i in range(repeticiones):
        print('------------------------------------------')
        print('Tiempo Activo')
        temporizador(activo)
        if i != (repeticiones - 1):
            print('------------------------------------------')
            print('Descanso')
            temporizador(descanso)
    print('------------------------------------------')
    print('Pomodoro Finalizado')
    print('------------------------------------------')
        
    
    
while True:
	print('------------------------------------------')
	print('Seleccione la opcion que desea utilizar: ')
	print('1.- Temporizador')
	print('2.- Pomodoro')
	print('3.- Salir')
	print('------------------------------------------')
	opcion = input('Ingrese una opcion: ')
	if opcion == '3':
		print('Gracias Por Utilizar la Aplicación')
		break
	elif opcion == '1':
		minutos = input('Ingrese el tiempo en minutos: ')
		tiempo = float(minutos) * 60
		temporizador(tiempo)
		print('')
		print('------------------------------------------')
	elif opcion == '2':
		pomodoro()
	else:
		print('Ingreso una Opcion Incorrecta')
     


