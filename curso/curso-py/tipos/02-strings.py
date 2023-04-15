# string es una cadena de texto tipo str
# 
nombre_curso = "Ultimate Python"
nombre_curso_otro = 'mi otro Ultimate Python'

print(nombre_curso + " " + nombre_curso_otro)

# string con salto de lineas tambien con \n
description_curso = """   
ultimate curso es la descripcion del string
"""
print(nombre_curso, description_curso)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")                       # esta es la mejor manera con la f

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] # imprime del 1 al 3 ----- 0 1 2 3 4 5 
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]   # pilla todos y saca el 0 2 4    pilla un rango y va de 2 en 2
print(language_slice)

# Reverse

reversed_language = language[::-1]   # al final no hay 0 al ir al reves empieza en el -1
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())    # pone la primera en mayuscula
print(language.upper())         # todo mayusculas
print(language.count("t"))      # cuenta cuantas ves apareca la letra
print(language.isnumeric())     # nos dice si es numero, True o False
print("1".isnumeric())          # nos dice si es numero, True o False
print(language.lower())         # todo minusculas
print(language.lower().isupper())   # lo pasa a minusculas y despues dice si es mayusculas
print(language.startswith("Py"))    # le está preguntando si Python empieza por Py
print("Py" == "py")             # No es lo mismo


# TABULACION \t con \\ escapamos del escape 

string_con_tabulacion = "\t este es un strig con tabulacion"
print (string_con_tabulacion)

#SALTO LINEA \n

print (len(nombre_curso))
print (nombre_curso[0])
print (nombre_curso[1])
print (nombre_curso[0:8])
print (nombre_curso[9: ])
print (nombre_curso[9: ])
print (nombre_curso[:8])
print (nombre_curso[ :8])

print (nombre_curso[:])
