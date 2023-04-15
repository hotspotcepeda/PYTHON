# metodo es una funcion que se encuentra en un metodo

animal = " Chanchito Feliz "

print(animal.strip().upper())  # print en mayusculas + quitar espacios del principio y final

print(animal.upper()) # print en mayusculas

print(animal.lower()) # print en minusculas

print(animal.capitalize()) # print capital solo mayusculas la primera

print(animal.title()) # la primera de cada palabra en mayusculas y el resto en minusculas

print(animal.strip()) # quita espacios en blanco del principio y del final

print(animal.strip().capitalize()) #concatenacion de quitar espacios en blanco del principio y final y poner SOLO la primer letra en mayusculas.

print(animal.rstrip()) #SACA ESPACIOS EN BLANCO DE A LA DERECHA 

print(animal.lstrip()) #SACA ESPACIOS EN BLANCO DE A LA IZQUI

print(animal.find("Jo")) #  busca una cadena de caracteres devuelve el indice  -1 significa que no lo encuentra

print(animal.find(" C")) #  busca una cadena de caracteres devuelve el indice del primer caracter de la cadena que estamos buscando

print(animal.find(" ")) #  busca una cadena de caracteres devuelve el indice del primer caracter de la cadena que estamos buscando

print(animal.replace("ch", "fl")) # reemplaza caracteres se ponen 2 argumentos  separados por COMA, y distingue mausculas

print(animal.replace("c", "f")) # reemplaza caracteres se ponen 2 argumentos  separados por COMA, y distingue mausculas

print(animal.replace("h", "l")) # reemplaza caracteres se ponen 2 argumentos  separados por COMA, y distingue mausculas

print(animal.strip().upper())  # print en mayusculas + quitar espacios del principio y final

print("CHan" in animal)

print("Chan" in animal)

print("CHan" not in animal)                 # entregan boolean de si encuentra en caracter/es o no

print("Chan" not in animal)

