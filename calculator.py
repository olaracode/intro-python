# Definir una funcion calculadora que pueda ejecutar suma, resta, division y multiplicacion


def suma(num_1, num_2):
    print(num_1 + num_2)


def resta(num_1, num_2):
    print(num_1 - num_2)


def division(num_1, num_2):
    print(num_1 / num_2)


def multiplicacion(num_1, num_2):
    print(num_1 * num_2)


def result_divider():
    print("=" * 5, "resultado", "=" * 5)


# Calculadora
def calculator():
    ## Recibir dos inputs con los valores
    ## Necesita Preguntarle al usuario que operacion realizar
    ## Y necesita realizar la operacion de acuerdo a lo anterior
    num_1 = float(input("Introduzca el primer numero: "))
    num_2 = float(input("Introduzca el segundo numero: "))

    operacion = int(
        input(
            """
        Que operacion desea realizar(1 - 4):
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        """
        )
    )
    print(num_1, num_2, operacion)
    ## ==
    if operacion == 1:
        result_divider()
        suma(num_1, num_2)
    elif operacion == 2:
        result_divider()
        resta(num_1, num_2)
    elif operacion == 3:
        result_divider()
        multiplicacion(num_1, num_2)
    elif operacion == 4:
        result_divider()
        division(num_1, num_2)
    else:
        print("Operacion no permitida")


running = True
print("=" * 5, "Bienvenido a mi super cool calculadora", "=" * 5)
while running:
    calculator()
    again = input("Otro calculo? y/n")
    if again != "y":
        running = False
        print("=" * 5, "Hasta Luego", "=" * 5)
