# for cumple múltiples funciones pero principalmente se utiliza para iterar una lista de elementos

for numero in range(5): # range(5) es un ITERABLE las LISTAS los STRINGS y las TUPLAS tambien son iterables.
    print(numero)
for numer in range(5):     
    print(numer, numer * 'hola mundo ')
    
#for else

buscar = 3

for number in range(5): 
    if number == buscar:
        print("encontrado", buscar)
        
buscar = 3

for number in range(5): 
    print(number)
    if number == buscar:
        print("encontrado", buscar)
        break#Con break se detiene la búsqueda cuando encuentra el resultado
    
#Aquí otro ejemplo realmente útil donde buscamos el número 100 entre 100000 números
buscar = 5

for number in range(10): 
    print(number)
    if number == buscar:
        print("encontrado", buscar)
        break #Con break se detiene la búsqueda cuando encuentra el resultado, En el siguiente ejemplo voy a hacer la misma búsqueda del númerosin el break 
    #y va a recorrer todos los números hasta 100000
    
buscar = 5

for number in range(10): 
    print(number)
    if number == buscar:
        print("encontrado", buscar)
        #break     

#Por ejemplo si estamos buscando un número con for y no lo encontramos podemos poner una solución a ese problema con else
        
buscar = 11

for number in range(5): 
    print(number)
    if number == buscar:
        print("encontrado", buscar)
        break
else:
    print("Numero no encontrado")    
    
buscar = 1

for number in range(5): 
    print(number)
    if number == buscar:
        print("encontrado", buscar)
        break
else:
    print("Numero no encontrado")    
    
    
    
for char in "Ultimate Python":     #Con esto lo que hacemos es imprimir todos los caracteres de la cadena uno por uno
    print(char)


print("Mouredev" * 41)






# for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for 



my_list = [35, 24, 62, 52, 30, 30, 17]
print("print my_list", my_list)

for element in my_list:                                         
    print("este for se va a ejeccutar tantas veces como elementos tenga", element)   # este for se va a ejeccutar tantas veces como elementos tenga

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
    