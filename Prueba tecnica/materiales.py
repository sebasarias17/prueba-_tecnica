class Material:
        nombre = ''
        codigo = int()
        valor = int()
        cantidad = int()

class Producto(Material):
        nombre = int()
        codigo = int()
        productos = [Material]

        def calc_valor(self):
            arr_productos = self.productos
            suma = sum(arr_productos)
            return suma

while True:
    print("Ingrese una opcion:")
    print("1. crear un producto con materiales")
    print("2. imprimir productos y materiales")
    print("4. modificar productos")
    print("5. salir")

    opcion = int(input())
    if opcion == 1:
            producto = Producto()
            print("Ingrese el nombre del producto")
            producto.nombre = input('')
            print("Ingrese el codigo del producto")
            producto.codigo = int(input())

            print("INGRESE LOS MATERIALES DEL PRODUCTO")

            material = Material()
            print("Ingrese el nombre del material")
            material.nombre = (input())
            print("Ingrese el codigo del material")
            material.codigo = int(input())
            print("Ingrese el vaor del material")
            material.valor = int(input())
            print("Ingrese la cantidad del material")
            material.cantidad = int(input())
            producto.productos = [material.nombre]
            
            print("Se ha creado el producto: ", producto.nombre, " Con los materiales", material.nombre)
    if opcion == 3:
           print(producto.nombre)
           print(producto.productos)
    if opcion == 4:
            producto = Producto()
            print("Ingrese el nuevo nombre del producto")
            producto.nombre = input('')
            print("Ingrese el nuevo codigo del producto")
            producto.codigo = int(input())

            print("INGRESE LOS NUEVOS MATERIALES DEL PRODUCTO")

            material = Material()
            print("Ingrese el nuevo nombre del material")
            material.nombre = (input())
            print("Ingrese el nuevo codigo del material")
            material.codigo = int(input())
            print("Ingrese el nuevo valor del material")
            material.valor = int(input())
            print("Ingrese la nueva cantidad del material")
            material.cantidad = int(input())
            producto.productos = [material.nombre]
            
            print("Se ha modificado el producto: ", producto.nombre, " Con los materiales", material.nombre)
    if opcion == 5:
           break