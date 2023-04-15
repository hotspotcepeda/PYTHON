mascotas = [
    "pancho", 
    "pincho", 
    "puncho", 
    "pencho", 
    "pancho", 
    "poncho"
]
print(mascotas)

#Con el insert agregamos un elemento al array, tenemos que indicar el índice donde queremos que entre el elemento
mascotas.insert(1, "melvin")

print(mascotas)

#Agregamos un elemento al final del array

mascotas.append("punchaco final")

print(mascotas)

# Para eliminar un elemento de la array lo haremos con el remove pero ojo si está repetido va eliminar solo la primera coincidencia.

mascotas.remove("pancho")

print(mascotas)

# También podemos usar pop para eliminar directamente el último elemento del array y sin conocerlo También se le puede pasar un índice

mascotas.pop()

print(mascotas)

#Aquí le estoy pasando un índice a pop y me va a eliminar el elemento correspondiente con el índice que esté dentro del array


mascotas.pop(0)

print(mascotas)

#Esto también lo podemos hacer con el del Le pasamos el índice y lo elimina

del mascotas[4]

print(mascotas)

# Con clear eliminamos todo el contenido del array eliminamos todos los elementos del array

mascotas.clear()

print(mascotas)