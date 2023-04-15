# El siguiente if respondeen base a si la edad cumplecon el true el false
# Las evaluaciones se hacen de arriba a abajo es importante seguir un orden

edad = input("Ingrese su edad ")
edad = int(edad)
if edad > 65:
    print("Usted puede ver la pelicula con super descuento") #Súper importante la indentación si no la colocamos no va a funcionar nada
elif edad > 54:
    print("Puedes ver la pelicula con descuento")
elif edad > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes entrar.")
    print("Ve a otro lado.")
print("Listo")


# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=21442 https://youtu.be/Kp4Mvapo5kc?t=21442 https://youtu.be/Kp4Mvapo5kc?t=21442 https://youtu.be/Kp4Mvapo5kc?t=21442 

### Conditionals ###

# if

my_condition = False

if my_condition:                                    # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")