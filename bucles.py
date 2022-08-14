# Lo primero que hay que hacer es definir una funcion como principal
def run():
    LIMITE = 1000 # Debemos establecer una CONSTANTE que en este caso servira para detener el programa, siempre se pone la palabra en mayuculas

    contador = 0 # El contador inicia en 0
    potencia_2 = 2**contador # Tambien debemos agregar la variable con el numero y la operacion para comenzar
    while potencia_2 < LIMITE: # El ciclo while nos servira para ejecutar la funcion hasta llegar al limite establecido anteriormente
        print('2 elevado a la ' + str(contador) + ' es igual a: ' + str(potencia_2))# Este es el mensaje que se le mostrara al usuario hasta que la condicion se rompa
        contador = contador + 1 # Si el contador no cambia la funcion queda en un loop infinito, esta variable nos ayuda a alcanzar el limite
        potencia_2 = 2**contador # esta variable tambien debe cambiar en cada loop para mostrar un valor diferente en cada vuelta

# Hecemos el llamado a nuestra funcion principal
if __name__ == '__main__': 
    run()