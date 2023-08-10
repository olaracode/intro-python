# Objetos en python
# Objetos en python son completamente distintos a los objetos en javascript
# Los objetos en javascript se definen asi { key: value }
# En python los objetos se definen con clases
# Las clases nos permiten crear instancias de elementos


## clase de calculadora


class BasicCalculator:
    def sum(a, b):
        print(a + b)

    def subs(a, b):
        print(a - b)

    def multiply(a, b):
        print(a * b)

    def division(a, b):
        print(a / b)


# BasicCalculator.sum(1, 2)  #
# BasicCalculator.subs(2, 2)  #
# BasicCalculator.division(2, 2)
# BasicCalculator.multiply(2, 2)


## Son extensibles
class AdvancedCalculator(BasicCalculator):
    # sum | subs | division | multiply -> Heredado de BasicCalculator
    def sqrRoot(a, b):
        print("Raiz Cuadrada de", a, b)


# AdvancedCalculator.sqrRoot(1, 2)


class Vehicle:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand
        self.year = year

    def acelerar(self):
        print("Vehiculo acelerando:", self.model)

    def frenar(self):
        print("Vehiculo frenando", self.model)

        ## Reemplazar lo que imprimes cuando imprimes la instancia

    def __repr__(self):
        ## Gracias pana jose <3
        return str(self.__dict__)


class Car(Vehicle):
    def __init__(self, model, brand, year, rin_size, paint_color, car_type):
        # Super le dice al objeto del que hereda cuales son los valores que le vamos a pasar
        super().__init__(model, brand, year)
        self.rin_size = (rin_size,)
        self.paint_color = paint_color
        self.car_type = car_type

    def corneta(self):
        print("sonido de corneta de", self.model)

    def serialize(self):
        return {"marca": self.brand, "model": self.model, "año": self.year}


class Bike(Vehicle):
    def __init__(self, brand, model, year, cilindraje, type):
        super().__init__(brand, model, year)
        self.cilindraje = cilindraje
        self.type = type

    def se_atraviesa(self):
        print("Moto de marca:", self.brand, "se atraviesa")


class Humano:
    def __init__(self, nombre, apellido, nacionalidad, edad, color_pelo, color_ojos):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.edad = edad
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos

    def descripcion(self):
        print("Soy un humano con ojos", self.color_ojos, "y pelo", self.color_pelo)


jose_morrone = Humano("Jose", "Morrone", "Venezolano", 22, "negro", "marrones")
ana_plata = Humano("Ana", "Plata", "Venezolana", 22, "marrones", "negro")

jose_morrone.descripcion()
ana_plata.descripcion()
