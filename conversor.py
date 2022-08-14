# Este programita es sencillo, convierte una cantidad en x de pesos a dolares, y no solo eso, el usuario puede elegir que a tipo de pesos hacer la conversion

# Este es el menu principal que le pregunta al usuario que tipo de moneda desea convertir a dolares
menu = """ 
Bienvenido al conversor de monedas 💰

Elige una opcion

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

"""

# Esta es la funcion a la que se le meten 2 parametros, el primero es el mensaje que se le va a mostrar al usuario y el segundo es el valor en dolares
def conversion(mensaje, valor_dolar):
    pesos = float(input(mensaje))# Se le solicita al usuario que ingrese el monto a convertir
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)# Aqui simplemente estamos diciendole al programa que muestre la variable dolares con 2 decimales
    dolares = str(dolares)# Convierte la variable de un float en un string
    print("Tienes $" + dolares)# Se le muestra al usuario la cantidad en dolares correspondiente al monto que ingreso
    return dolares


opcion = int(input(menu))# Hacemos el llamado a nuestra variable menu

if opcion == 1:
    conversion("Cuantos pesos traes menor?: ", 4000)
elif opcion == 2:
    conversion("Cuantos pesos trae boludo?: ", 70)
elif opcion == 3:
    conversion("Cuantos pesos trae chamaco?: ", 30)
else:
    print("Ingresa una opcion valida puto")

