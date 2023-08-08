# Para escribir comentarios se usa(#)
# print = console.log() | Una herramienta para escribir en la consola
# print("Hello World")

# variables
# nombre_variable = valor_de_variable
# snake_case = snake_case separa todas las palabras con un piso y todo en minuscula

# Python:
# Es un lenguaje interpretado
# Es un lenguaje debilmente tipado
# Normalmente se trabaja con OOP(Object Oriented Programming)


# String
hello_message = "Hello World"

# Integer | Numeros
num_1 = 1

# Float
num_2 = 1.2

# Booleanos True | False
is_active = True
is_not_active = False

# Array = List | [elements]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Objetos(Python Programacion Orientada a Objetos(python))
# { "key": "value" }

# objeto de javascript = diccionario de python
car = {"n_seats": 4, "brand": "Volvo", "model": "yo que se", "year": 2018}


# print(hello_message)
# print("Integer", num_1)
# print("Float", num_2)
# print("Booleano", is_active, is_not_active)
# print("List", num_list)
# print("Dictionary", car)


#
# print("Suma(5 + 5):", 5 + 5)
# print("Resta(5 - 5):", 5 - 5)
# print("Division(10/2):", 10 / 2)
# print("Division(10%2) modulo:", float(10 % 2))
# print("Multiplicacion(2 * 2.5):", int(2 * 2.5))  # Te devuelve un float
# print(bool(0))

# print("Suma: " + str(5 + 5))
## Para convertir de un tipo de dato tenemos
# a String -> str()
# a integer -> int()
# a float -> float()
# a bool -> bool()


# Funciones def suma(): | function suma(){}
# def nombre_funcion(parametros):
#   funcion
# Es sensible a las indentaciones | identaciones
def suma(num1, num2):
    return num1 + num2


def reste(num1, num2):
    print(num1 - num2)


# print(suma(1, 2))
# reste(2, 4)


# condicionales | Controles de flujo
def is_underage(age):
    # Si es menor de 18 años dile que no puede entrar
    # Si es mayor de 18 años dile que si puede entrar

    # if condicion:
    #   Bloque indentado de codig
    if age < 18:
        print("eres un menor, pa tu casa")

    # else:
    #   Bloque indentado de codigo
    else:
        print("Bienvenido mi pana")


# is_underage(18)
# is_underage(16)

cohorte_44 = ["Luis", "Jose Carlos", "Manuel", "Juan", "Ana"]


def show_students(student_list):
    for student in student_list:
        print(student)


show_students(cohorte_44)


# for(let i = 0; i < condicion; i++){}
# for i in range(10):

for i in range(10):
    print("hola", i)

for item in [0, 1, 2, 3, 4]:
    print(i)

cars = ["Volvo", "Toyota"]

for car in cars:
    print(car)

# While

i = 0
# while condicion:
#   bloque indentado
while i < 10:
    print("while", i)
    i = i + 1

## Command Line Interface

lang = input("Que lenguaje: ")
