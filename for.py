# def run():
#    LIMITE = 1000
#
#    contador = 0
#
#    while contador <= LIMITE:
#        print(str(contador))
#        contador += 1


# def run(): #definimos funcion principal
#    for contador in range(1000):#utilizamos ciclo for con una variable llamada contador que inicia en 0 y termina en 999
#        print(contador)#muestra en la consola el resultado hasta que se llgue al limite de 1000
#
# if __name__ == '__main__':# inicio del programa
#    run()



def run():

#    nombre = input("Escribe tu nombre carechimpa: ") # solicita una variable en formato string al usuario
#    for letra in nombre: # hace un recorrido caracter por caracter del dato suministrado por el usuario
#        print(letra) # muestra el resultado

    frase = input("Escribe una frase pelmazo: ")
    for caracter in frase:
        print(caracter.upper()) # muestra el caracter en mayusculas


if __name__ == '__main__':
    run()