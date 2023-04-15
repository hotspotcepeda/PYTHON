# LISTAS  permite insercion recolocacion, modificacion // ARRAIS == vector //  ARREGLOS 

numeros = [1, 2, 3] #Lo que está entre corchetes es el contenido de la lista y puede ser como queramos de largo

letras = ["a", "b", "c"]

palabras = ["chanchi", "feliz"]

palabrasFelices = ["chanchi", "feliz", "Felipus", "pijus"]

booleans = (True, False, True,  False)

matriz = [[0, 1], [1, 1], [1, 0] ]  # Una matriz es un listado que contiene más listados

ceros = [0,0,0,0,0,0,0,0,0,0]  #Que estamos creando una matriz que contiene 10 ceros

ceros0 = [0] * 10    #De nuevo creamos una matriz que contiene 10 ceros lo que hacemos es multiplicar el 0 por 10 veces

ceros0y1 = [0, 1] * 10  

# Sí por ejemplo quiero tener dos listas y quiero juntarlas en una súper lista que contenga todas las listas....

superlista = numeros + letras  #  Estamos tomando las dos listas

#rango

rango = list (range(10)) #Lista de 10 números que empieza por el cero
rangoDel1 = list (range(1, 11)) #Lista de 10 números que empieza por el 1

print(numeros)
print(letras)
print(palabras)
print(palabrasFelices)
print(booleans)
print(matriz)
print(ceros)
print(ceros0)
print(ceros0y1)
print(superlista)
print(rango)
print(rangoDel1)

#Creamos listas de strings

chars = list("Hola Mundo")
print(chars)


### Lists ###  mouredevmouredevmouredevmouredevmouredevmouredevmouredevmouredevmouredevmouredevmouredevmouredevmouredevmouredevmour
print("mouredev" * 35)
# Definición

my_list = list()         # ojo que no es tupla, está definiendo una lista con parentesis poniendo list
my_other_list = []       # Lista con braquets

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print("count", my_list.count(30))  # cuenta las veces que se repite el 30 en my_list
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")    # con append INSETA al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo")     # con insert 1 inserta en la posicion 1
print(my_other_list)

my_other_list[1] = "Azul"           
print(my_other_list)

my_other_list.remove("Azul")        # se cepilla el campo mencionado, Azul
print(my_other_list)

my_list.remove(30)                  # elimina el primer 30 que encuentra
print(my_list)

print(my_list.pop())                # elimina el último elemento por defecto y ademas almacena el valor eliminado
print(my_list)

my_pop_element = my_list.pop(2)     # elimina el elemento y ademas almacena el valor eliminado en una variable my_pop_element
print(my_pop_element)               # se puede volcar el elemento a otra lista
print(my_list)

del my_list[2]                      # elimina el valor del elemento 2 y desaparece
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()        # copia la lista en otra lista my_new_list

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()               # invierte orden
print(my_new_list)

my_new_list.sort()                  # ordena de manor a mayor ,,   se puede poner luego un REVERSE
print(my_new_list)

# Sublistas

print(my_new_list[1:3])             # rebanadas, con los indices

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))



