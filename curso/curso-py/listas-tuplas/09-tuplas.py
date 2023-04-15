# Una tupla es lo mismo que una lista pero no se pueden crear ni modificar elementos. llevan () en lugar de []

# no admiten ni apend ni pop no son modificables. SON INMUTABLES.

numeros = (2, 4, 7, 66, 33, 3, 5, 100) + (33, 3, 5, 100)
print(numeros)


punto = tuple([2, 4, 7, 66])
print(punto)

menosNuemeros = numeros[:2]    # entrega otra tupla que toma solo las 2 primeras posiciones de numeros
print(menosNuemeros)

primero, segundo, *otros = numeros
print(primero, segundo, *otros)

# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711https://youtu.be/Kp4Mvapo5kc?t=14711https://youtu.be/Kp4Mvapo5kc?t=14711https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ###

# Definición

my_tuple = tuple()      # le pido hacer una tupla
my_other_tuple = ()     # solo con poner los parentesis () ya es tupla

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])                  # devuelve el valor de la posicion seguin indice 0 1 2 3 4 5 6                
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print("count", my_tuple.count("Brais"))     # cuenta las veces que encuentra el valor
print("index", my_tuple.index("Moure"))     # entrega el indice del valor       
print("index", my_tuple.index("Brais"))     # como está repetido entrega el primer indice que encuentra

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple    # sumo una tupla con otra y la asigno a otra tupla pero no las estoy modificando
print(my_sum_tuple)

# Subtuplas

print("nos entrega los elementos del 3 al 6", my_sum_tuple[3:6])                    # nos entrega los elementos del 3 al 6

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)                   # reasigno una tupla en una lista
print(type(my_tuple))                       # ahora es tipo list

my_tuple[4] = "MoureDev"                    # ahora como es lista le inserto un elemento mas en la posicion 4
my_tuple.insert(1, "Azul")                  
my_tuple = tuple(my_tuple)                  # ahora convierto la lista en tupla, de nuevo inmutable 
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion   NO deja hacer un del de un elemento porque es una modificación

del my_tuple                                # del de la tulpa completa si que admite.


# print(my_tuple) NameError: name 'my_tuple' is not defined