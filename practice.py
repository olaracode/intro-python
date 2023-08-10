# FizzBuzz
# Cuente de 0 a 100
# cuando el numero sea divisible entre 3 y 5 imprima FizzBuzz
# cuando el numero sea divisible entre 3 que imprima fizz
# cuando el numero sea divisible entre 5 que imprima buzz
# cuando no sea divisible entre ninguno que imprima el numero


# range(start: punto de inicio, stop: punto de fin, step: cantidad)
# Parametros
def fizz_buzz():
    # recibir el valor del usuario a traves de la terminal
    quantity = int(input("Juega a FizzBuzz! Cuantas veces? "))
    fizz_buzz_counter = 0
    fizz_counter = 0
    buzz_counter = 0
    for iteracion in range(quantity):
        if iteracion % 3 == 0 and iteracion % 5 == 0:
            print("FizzBuzz")
            fizz_buzz_counter += 1
        elif iteracion % 3 == 0:
            print("Fizz")
            fizz_counter += 1
        elif iteracion % 5 == 0:
            print("Buzz")
            buzz_counter += 1
        else:
            # Defecto
            print(iteracion)
    print("Conteo de Buzz:", buzz_counter)
    print("Conteo de Fizz:", fizz_counter)
    print("Conteo de FizzBuzz:", fizz_buzz_counter)


# Una funcion, que reciba una lista de estudiantes [x]
# Que cuente cuantos estudiantes hay en total [x]
# Que cuente cuantos estdudiantes tienen un nombre que comienza por A [x]
# Que cuente cuantos estudiantes tienen un nombre que termina por la letra o
# 1 Iterar los estudiantes
# 2 Verificar si la primera letra es A
# 2.1 Obtener la primera letra
# 2.2 Agregar al contador


def student_control(student_list):
    # pass es el modo de tener una funcion vacia
    print("Total de estudiantes:", len(student_list))

    # for iterador en elemento_a_iterar
    student_a_counter = 0
    student_o_counter = 0

    for student in student_list:
        first_letter = student[0]
        if first_letter == "a":
            student_a_counter += 1

        last_letter = student[-1]
        if last_letter == "o":
            student_o_counter += 1

    print(student_a_counter, "de estudiantes con la letra a al principio")
    print(student_o_counter, "de estudiantes con la letra o al final")


print("Hola")
students = ["andres", "ana", "juan", "antonio", "pedro", "jose", "ana", "ana"]
student_control(students)

print("antes:", students)

## Listas
## lista.append(nuevo_elemento) -> agrega un elemento al final
students.append("jose carlos")

print("despues:", students)

## Lista.pop() -> Elimina el ultimo elemento
students.pop()
print(students)

## Lista.remove(elemento_a_eliminar)
# students.remove("ana")
print(students)

## lista.reverse() -> revierte el orden del arreglo
students.reverse()
print(students)

## lista.sort() -> ordena el arreglo
students.sort()
print(students)

## lista.count(elemento_a_contar) -> da la cantidad de elementos con el elemento a contar
print(students.count("ana"))
print("a en ana".count(" "))
