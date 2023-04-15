# Set significa grupo o conjunto.
# los set no se encuentran ordenados ni podemos acceder a sus elementos por su indice porque NO ESTAN ORDENADOS  (ordena elementos por algoritmo hash ) . 
# NO ADMITE REPETIDOS.


### Sets ###

# Definición

my_set = set()                          #definimos el set con set y los parentesis, de origen es un set
my_other_set = {}                       #definimos con llaves y ojo que cuando está vacio se consideta diccionario.

print(type(my_set))
print(type(my_other_set))               # Inicialmente es un array diccionario

my_other_set = {"Brais", "Moure", 35}   # Cuando le pongo valores se transforma en un set
print(my_other_set)
print(type(my_other_set))

print("nos entrega el numero de elentos del set", len(my_other_set))                # nos entrega el numero de elentos del set

# Inserción

my_other_set.add("MoureDev")                                    # agreganos un nuevo elemento y lo pone al principio

print("el add lo mete al principio", my_other_set)              # Un set no es una estructura ordenada

my_other_set.add("MoureDev")                                    # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("existe en el set = ", "Moure" in my_other_set)                                  # existe en el set True
print("no existe en el set = ", "Mouri" in my_other_set)                                  # no existe en el set False

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()                                                # Clear vacia todos los elentos del set
print(len(my_other_set))

del my_other_set                                                    # elimina set        
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Brais", "Moure", 35}                                     
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))