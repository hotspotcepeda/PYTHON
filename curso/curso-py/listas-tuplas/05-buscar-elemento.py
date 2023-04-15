mascotas = ["pancho", "pincho", "puncho", "pencho", "pancho"]


print(mascotas.index("pancho"))    # Devuelve el índice del elemento que estamos buscando

#Ahora vamos a hacer una búsque dadentro de la lista de un elemento que no sabemos si existe o no

if "pincho" in mascotas:
    print(mascotas.index("pincho"))
    
if "poncho" in mascotas:
    print(mascotas.index("poncho"))  #Aquí estoy buscando un elemento que no existe y no me devuelve nada
else:
    print("No encontrado") #Aquí cuando le pongo el else al if me devuelve el mensaje de que no ha encontrado lo que está buscando
    
    
    
#Para buscar las veces que se encuentra el elemento dentro del array utilizamosla siguiente fórmula

print(mascotas.count("pancho")) 

# De esta manera nos devuelve Solo de la primera vez que lo encuentra

if "pancho" in mascotas:
    print(mascotas.index("pancho"))  #Aquí estoy buscando un elemento que no existe y no me devuelve nada
