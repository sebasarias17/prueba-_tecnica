#Aplicación de consola con menu de 
#Seleccione la figura --> Ingresar dimenciones
import math

class Circle:
    radio = int() 
    def area_circle(self,radio):
        radio = self.radio
        area_c = (math.pi) * radio**2
        return int(area_c)

class Square:
    lado = int()
    def area_square(self,lado):
        lado = self.lado
        area_s = lado**2
        return int(area_s)

class Rectangle:
    base = int()
    altura = int()
    def area_rectangle(self,base,altura):
        base = self.base
        altura = self.altura
        area_r = (base * altura)
        print (int(area_r))

class Triangle:
    base = int()
    alura = int()
    def area_triangle(self,base,altura):
        base = self.base
        altura = self.altura
        area_t = (base * altura)/2
        return  int(area_t)

while True:
    print("Ingrese una opcion:")
    print("1. Circulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Triangulo")
    print("5. Salir")
    print("-------------")
    opcion = int(input())

    if opcion == 1:
        circulo = Circle()
        print("ingrese el radio:")
        circulo.radio = int(input())
        print(circulo.area_circle(circulo.radio))
    elif opcion == 2:
        cuadrado = Square()
        print("ingrese el lado:")
        cuadrado.lado = int(input())
        print(cuadrado.area_square(cuadrado.lado))
    elif opcion == 3:
        rectangulo = Rectangle()
        print("ingrese la altura:")
        rectangulo.altura = int(input())
        print("ingrese el la base:")
        rectangulo.base = int(input())
        print(" la respuesta es:")
        respuesta = rectangulo.area_rectangle(rectangulo.base,rectangulo.altura)
    elif opcion == 4:
        triangulo = Triangle()
        print("ingrese la altura:")
        triangulo.altura = int(input())
        print("ingrese el la base:")
        triangulo.base = int(input())
        print("la respuesta es:")
        print(triangulo.area_triangle(triangulo.base,triangulo.alura))
    elif opcion == 5:
        break



