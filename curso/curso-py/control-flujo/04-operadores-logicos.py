# and, or, not


# gas = True
# encendido = True         #OJO que si usamos el operador and ambos valores tienen que ser True

# print("Resultado True and True = ", gas and encendido)

# if gas and encendido:
#     print("Puedes avanzar tienes gas y está encendido")

# gaso = False
# encendidoo = True

# print("Resultado False or True = ", gaso or encendidoo)
# print("Resultado True or False = ", gaso or encendidoo)

# gasoo = False
# encendidooo = False

# print("Resultado False or True = ", gaso or encendidoo)
# print("Resultado True or False = ", gasoo or encendidooo)


# if gaso or encendidoo:
#     print("Puedes avanzar no tienes gaso anque esté encendido")


# gas = False
# encendido = True
# edad = 18

# if not gas and(encendido or edad > 17):
#     print("puedes avanzar ")

# operadores de cortocircuito and todas las evaluacion tienen que ser True, si la primera es False no la evalua. se ejecutan de izquierda a derecha


gas = False
encendido = True
edad = 18

if not gas and encendido and edad > 17:
    print("puedes conducir")

# en el caso de or solo hace falta una expresión para que se a True. Si la primer de la IZQUIERDA es True ya las demas no se evaluan

if not gas or encendido or edad > 17:
    print("puedes conducir")

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False

print("Operador \"and\":")


x = 5
y = 10
if x > 0 and y > 0:
    print("Ambos números son positivos")


print("Operador \"or\":")


x = 5
y = -3
if x > 0 or y > 0:
    print("Al menos uno de los números es positivo")


print("Operador \"not\":")


x = True
if not x:
    print("La variable x es False")
else:
    print("La variable x es True")
