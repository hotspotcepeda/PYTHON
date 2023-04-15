# no es buena practica utilizar varibles LOCALES intentaremos utilizar varibles LOCALES.

saludo = "Saludo Global !"  # definimos la variable de manera GLOBAL


def saludar():
    # print (saludo)           # da error porque la variable está sin definir
    saludo = "Hola mundo !"  # definimos la variabla de manera LOCAL
    print(saludo)


def saludaChanchito():
    saludo = "Hola chanchitor !"
    print(saludo)

# print(saludo)  #Arroja error porque el alcance no está definido


print(saludar)
print(saludaChanchito)


print(saludo)
saludar()
print(saludo)
saludaChanchito()
print(saludo)
saludar()
print(saludo)
