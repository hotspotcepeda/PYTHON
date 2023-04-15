# super utilizado  es como las BBDD nos entraga los datos   presenta realacion clave - valor
# son una coleccion de datos 


punto = {"x": 25, "y": 50}

print(punto)
print(punto["x"])
print(punto["y"])

punto ["z"] = 45        # agrego un elemento al diccionario
print(punto["z"])

print(punto)            # imprime el diccionario con el nuevo elemento. 


print(punto.get("x")) 
print(punto.get("y"))
print(punto.get("z"))

usuarios = [
    {"id": 1}
]
print("mouredev" * 42)
# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc https://youtu.be/Kp4Mvapo5kc https://youtu.be/Kp4Mvapo5kc https://youtu.be/Kp4Mvapo5kc https://youtu.be/Kp4Mvapo5kc 

### Dictionaries ###

# Definición

my_dict = dict()        # lo defino con llaves {} 
my_other_dict = {}      # Tambien lo puedo definir con {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},         # tiene un set dentro
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("estamos buscando Moure por clave y no por valor", "Moure" in my_dict)                            # estamos buscando por clave y no por valor  y es False
print("estamos buscando apellido por clave ", "Apellido" in my_dict)                                    # estamos buscando por valor y es True

# Inserción

my_dict["Calle"] = "Calle MoureDev"                 # agraega un nuevo campo al diccionario
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]                                # elimina elemento , NO SE PUEDE RECUPERAR
print(my_dict)

# Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))                          # crea un nuevo diccionario sin valores
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))              # No vale de mucho, genera diccionario pero sin valores
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))

