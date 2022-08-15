def run():
    
#    for numero in range(1000): # Empezamos el recorrido con la variable numero en cero y terminamos en 999
#        if numero % 2 == 0: # Si el numero es par se muestra
#            print(numero)
#            continue

    for numero in range(0,1001,2): # va mostrando los numeros desde el 0 de 2 en 2
        print(numero) 
        LIMITE = 10
        if numero == LIMITE: # Cuando llegue al numero de la variable limite se detiene el programa
            break

            


if __name__ == '__main__':
    run()