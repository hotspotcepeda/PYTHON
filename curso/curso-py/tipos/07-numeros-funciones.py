import math

print("redondeo con \"round\" al numero mas cercano a 1.3 = ", round(1.3))  # redondeo al numero mas cercano a 1.3

print("redondeo con \"round\" al numero mas cercano a 1.7 = ", round(1.7))  # de nuevo redondea al numero entero mas cercano 

print("redondeo con \"round\" al numero mas cercano a 1.5 = ", round(1.5))  

print("redondeo con \"round\" al numero mas cercano a 1.49 = ", round(1.49))  


# abs entrega el valor absoluto , saca el + y el - del numero y devulve el positivo

print("El valor absoluto con \"abs\" del numero -50 es", abs(-50))

print("El valor absoluto con \"abs\" del numero 70 es", abs(70))


# Lamentablemente en Python no tiene muchas funcionalidades matemáticas entonces lo que hay que hacer es importar el módulo correspondiente 
# en este caso el módulo de las matemáticas
# Un módulo es un archivo que nosotros podemos traer y que tiene implementados funciones y metodos
# Para traerhoy importarun módulolo hacemos con el comando import por ejemplo import math

#Estas funciones ya me las estoy trayendo del módulo MATH Esto lo hago Importando la librería con # import math

import math  #Aquí lo que hago es importar la librería math

print("\nFUNCIONES DEL MODULO math")

print("\n\nENTERO MAS CERCANO SUPERIOR\nToma el número 1.1 y lo lleva al número superior entero más cercano usando la funcion \"ceil\" el resultado es : ", math.ceil(1.1)) # Toma el número y lo lleva al número superior entero más cercano

print("ENTERO MAS CERCANO INFERIOR\nToma el número 1.999 y lo lleva al número inferior entero más cercano usando la funcion \"floor\" el resultado es : ", math.floor(1.999)) # Toma el número y lo lleva al número inferior entero más cercano

print("COMPROVACION DE NUMERO\nToma el número qué le pasemos y comprueba si NO es un número usando la funcion \"isnan\". \nAquí la estoy pasando un número decimal 1.999 y me dice que es false usando la funcion \"isnan\" el resultado es : ", math.isnan(1.999)) # Toma el número que le pasemos y comprueba si NO es un número

print("COMPROVACION DE NUMERO\nToma el número qué le pasemos y comprueba si NO es un número. Aquí la estoy pasando un número entero 30 y me dice que es false \npor la tanto es falso que no es un numero y es verdad que es un numero !!!\n usando la funcion \"isnan\" el resultado es : ", math.isnan(30)) # Toma el número que le pasemos y comprueba si NO es un número

print("POTENCIA\nToma el número 10 y lo Eleva a la potencia 3 usando la funcion \"pow\" el resultado es 10*10*10 : ", math.pow(10, 3)) # Toma el número y lo Eleva a su potencia

print("RAIZ CUADRADA\nToma el número 9 y nos entrega la raiz cuadrada usando la funcion \"sqrt\" el resultado es raiz cuadrada de 9 : ", math.sqrt(9)) # Toma el número y entrega raiz cuadrada

print("\nFUNCIONES DEL MODULO math\nPodemos ver todas las funciones del modulo \"math\" en la web https://docs.python.org/3/library/math.html ")

