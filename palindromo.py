# Un palindromo es una oracion o palabra que puede leerse igual tanto de inicio a fin como de fin a inicio
# Ejemplo: "Luz azul" se lee igual que "luza zuL"

def palindromo(palabra):
    palabra = palabra.replace(' ', '') # Quitamos los espacios en caso de que sea una oracion con varias palabras
    palabra = palabra.lower()# Lo ponemos todo en minusculas para que el programa no se confunda, el case sensitive siempre esta encendido para las maquinas
    palabra_invertida = palabra[::-1]# Al invertir los caracteres que escribe el usuario debemos guardarlo en una variable
    if palabra == palabra_invertida:# Comparamos las variables para saber si se leen igual en ambos sentidos
        return True 
    else:
        return False


def run(): # Definimos nuestra funcion principal
    palabra = input('Escribe una palabra: ')# Le solicitamos al usuario que ingrese datos
    es_palindromo = palindromo(palabra)# Hacemos el llamado a la funcion que verifica si se cumple o no la condicion

    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':# Esta es la manera correcta con la que se deben iniciar todos los programas en Python
    run()