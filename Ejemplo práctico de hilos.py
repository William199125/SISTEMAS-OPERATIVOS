# Vamos a realizar una calculadora en donde se va a realzar varias tareas o en este caso operaciones en donde cada hilo cumplira una funcion especifica 
import threading

# Funciones para las operaciones matemáticas
def sumar(a, b):
    print(f"La suma de {a} y {b} es {a + b}")

def restar(a, b):
    print(f"La resta de {a} y {b} es {a - b}")

def multiplicar(a, b):
    print(f"La multiplicación de {a} y {b} es {a * b}")

def dividir(a, b):
    if b != 0:
        print(f"La división de {a} entre {b} es {a / b}")
    else:
        print("No se puede dividir entre cero")

# Crear hilos para realizar las operaciones
hilo_suma = threading.Thread(target=sumar, args=(5, 3))
hilo_resta = threading.Thread(target=restar, args=(10, 4))
hilo_multiplicacion = threading.Thread(target=multiplicar, args=(6, 7))
hilo_division = threading.Thread(target=dividir, args=(20, 4))

# Iniciar los hilos
hilo_suma.start()
hilo_resta.start()
hilo_multiplicacion.start()
hilo_division.start()

# Esperar a que todos los hilos terminen
hilo_suma.join()
hilo_resta.join()
hilo_multiplicacion.join()
hilo_division.join()

print("Todas las operaciones han sido completadas.")
