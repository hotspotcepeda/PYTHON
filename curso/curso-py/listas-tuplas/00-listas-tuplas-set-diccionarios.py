# Listas: Las listas son colecciones ordenadas y mutables de elementos. 
# Se pueden acceder a sus elementos mediante un índice y se pueden modificar, añadir o eliminar elementos.

# Tuplas: Las tuplas son colecciones ordenadas e inmutables de elementos. Una vez creada, no se pueden modificar.
# Se puede acceder a los elementos mediante un índice.

# Diccionarios: Los diccionarios son colecciones no ordenadas de pares clave-valor. 
# Se accede a los elementos mediante su clave y se pueden modificar, añadir o eliminar elementos.

# Sets: Los sets son colecciones no ordenadas y sin elementos duplicados. 
# Se pueden realizar operaciones de conjunto, como unión, intersección y diferencia.


# Ejemplo de listas
mi_lista = [1, 2, 3, 4]
mi_lista.append(5)
print(mi_lista)

# Ejemplo de tuplas
mi_tupla = (1, 2, 3, 4)
print(mi_tupla[1])

# Ejemplo de diccionarios
mi_dict = {"nombre": "Juan", "apellido": "Pérez", "edad": 30}
print(mi_dict)
print(mi_dict["nombre"])

# Ejemplo de sets
mi_set = set([1, 2, 3, 4, 4])
print(mi_set)