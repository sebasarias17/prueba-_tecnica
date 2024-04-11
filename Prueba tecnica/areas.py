import math

class Circle:
    def __init__(self):
        self.radio = 0

    def area_circle(self, radio):
        return int(math.pi * radio ** 2)

class Square:
    def __init__(self):
        self.lado = 0

    def area_square(self, lado):
        return lado ** 2

class Rectangle:
    def __init__(self):
        self.base = 0
        self.altura = 0

    def area_rectangle(self, base, altura):
        return int(base * altura)

class Triangle:
    def __init__(self):
        self.base = 0
        self.altura = 0

    def area_triangle(self, base, altura):
        return (base * altura) / 2

while True:
    print("Ingrese una opcion:")
    print("1. Circulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Triangulo")
    print("5. Salir")
    opcion = int(input())

    if opcion == 1:
        circulo = Circle()
        print("Ingrese el radio:")
        circulo.radio = int(input())
        print("Área del círculo:", circulo.area_circle(circulo.radio))
    elif opcion == 2:
        cuadrado = Square()
        print("Ingrese el lado:")
        cuadrado.lado = int(input())
        print("Área del cuadrado:", cuadrado.area_square(cuadrado.lado))
    elif opcion == 3:
        rectangulo = Rectangle()
        print("Ingrese la base:")
        rectangulo.base = int(input())
        print("Ingrese la altura:")
        rectangulo.altura = int(input())
        print("Área del rectángulo:", rectangulo.area_rectangle(rectangulo.base, rectangulo.altura))
    elif opcion == 4:
        triangulo = Triangle()
        print("Ingrese la base:")
        triangulo.base = int(input())
        print("Ingrese la altura:")
        triangulo.altura = int(input())
        print("Área del triángulo:", triangulo.area_triangle(triangulo.base, triangulo.altura))
    elif opcion == 5:
        print("Saliendo...")
        break
