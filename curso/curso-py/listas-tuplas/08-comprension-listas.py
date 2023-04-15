usuarios = [
    ["pancho", 4],
    ["pincho", 1],
    ["puncho", 9],
    ["pencho", 2]
]
print(usuarios)

#Vamos a extraer solamente el valor del nombre del array

nombres = []
for usuario in usuarios:       #Utilizando for podemos extraer el elemento tomando el indice de cada elemento.
    nombres.append(usuario[0])
print(nombres)


# name = [expresion for item in items]    map

name = [usuario[0] for usuario in usuarios] # De esta manera podemos tomar una lista y aplicar una transformación a cada 1 de los elementos que hay dentro de la lista
print(name)

#aquí estoy aplicando un filtro           filter
name = [usuario for usuario in usuarios if usuario[1] > 2] # Lo estoy pidiendo acceder al IDE [1] del usuario y comprobar si es mayor que dos
print(name)

#aquí estoy aplicando un filtro
name = [usuario for usuario in usuarios if usuario[1] > 7] # Lo estoy pidiendo acceder al IDE [1] del usuario y comprobar si es mayor que 7
print(name)

#aquí estoy aplicando un filtro y ademas modificando la lista usuarios       filter + map
name = [usuario[0] for usuario in usuarios if usuario[1] > 2] # Lo estoy pidiendo acceder al IDE [1] del usuario y comprobar si es mayor que 7
print(name)

#  map   ordenar con otro metodo
names = list(map(lambda usuario: usuario[0], usuarios))
print(names)

#  filter   filtrar con otro metodo
names_menos = list(filter(lambda usuario: usuario[1] > 7, usuarios))
print(names_menos)

