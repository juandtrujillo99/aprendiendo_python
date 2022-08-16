import random # incluimos una libreria a nuestro proyecto

def run():
    numero_aleatorio = random.randint(1, 100) # creamos una variable a la cual se le asigna un numero con la ayuda de la libreria
    numero_elegido = int(input("Escribe un numero: "))# se le solicita un valor al usuario

    while numero_elegido != numero_aleatorio: # se hace un ciclo que compara el numero del programa con el que el usuario ingreso
        if numero_elegido < numero_aleatorio:
            print("Escribe un numero mas grande")
        else:
            print("Escribe un numero mas pequeño")
        numero_elegido = int(input("Escribe otro numero: "))# se le da otro intento al usuario
    print("Ganaste prro")



if __name__ == "__main__":
    run()