# Vamos a generar una calculadora en la que el usuario ingrese un número y si no existe ya 
# después le pediremos un operador suma resta multi o divi 
# despues le pediremos que ingrese otro númeroy a continuación mostraremos el resultado 
# guardaremos el resultadoy lo imprimiremos en pantalla para usarlo en la siguiente operación

print("Bienvenido a la calculadora DORA")
print("Para salir de la calculadora escribe \"Salir\"")
print("Las operaciones disponibles son: \nSUMA + \nRESTA - \nMULTI * \ny DIV /")

resultado =""
while True:
    if not resultado:
        resultado = input("Ingresa número: ")
        if resultado.lower () == "salir":
            break
        resultado = int(resultado)
    operador = input("Ingresa operador: ")        
    if operador.lower () == "salir":
        break
    numero2 = input("Ingresa número: ")
    if numero2.lower () == "salir":
        break
    numero2 = int(numero2)
    
    if operador.lower() == "+":
        resultado += numero2
    elif operador.lower() == "-":
        resultado -= numero2
    elif operador.lower() == "*":
        resultado *= numero2
    elif operador.lower() == "/":
        resultado /= numero2
    else:
        print("Operacion no valida")
        break
        
    print(f"el resultado es: {resultado}")
    








      