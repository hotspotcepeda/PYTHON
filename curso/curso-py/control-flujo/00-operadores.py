# OPERADORES ARITMETICOS #

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(2 **3 + 3 -7 / 1 // 4)   # convimamos operaciones

print(10 % 3)   # modulo
print(10 // 3)  # flor division, hacemos la division y la aproxima a un numero entero
print("exponente de 2 ** 3 2*2*2 = ", 2 ** 3)   # calcula exponente

print("Hola" + " mundo.")  # pero el - no funciona como el + tampoco funciona sumando int + str
# no funciona --> print("Hola" - " mundo.") 
# no funciona --> print("Hola" + 5) 

print("sumando 2 str: Hola " + str (5))   
print("multiplicando str: Yeah por 3 " * 3)  
print("multiplicando str: Hola " * (2 ** 2))  

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
print('Multiplying complex numbers: ',(1 + 1j) + (1 - 1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)



