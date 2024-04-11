class Material:
    def __init__(self, nombre, codigo, valor, cantidad):
        self.nombre = nombre
        self.codigo = codigo
        self.valor = valor
        self.cantidad = cantidad

    def editar(self, nombre=None, valor=None, cantidad=None):
        if nombre:
            self.nombre = nombre
        if valor is not None:
            self.valor = valor
        if cantidad is not None:
            self.cantidad = cantidad

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.productos = []

    def agregar_material(self, material):
        self.productos.append(material)

    def calcular_valor(self):
        return sum(item.valor * item.cantidad if isinstance(item, Material) else item.calcular_valor() for item in self.productos)

    def editar(self, nombre=None):
        if nombre:
            self.nombre = nombre

materiales = {}
productos = {}

def agregar_material():
    nombre = input("Nombre del material: ")
    codigo = input("Código del material: ")
    valor = float(input("Valor del material: "))
    cantidad = int(input("Cantidad del material: "))
    materiales[codigo] = Material(nombre, codigo, valor, cantidad)
    print("Material agregado con éxito.")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    codigo = input("Código del producto: ")
    producto = Producto(nombre, codigo)
    while True:
        cod_material = input("Ingrese el código del material (deje en blanco para terminar): ")
        if not cod_material:
            break
        if cod_material in materiales:
            producto.agregar_material(materiales[cod_material])
        else:
            print("Material no encontrado.")
    productos[codigo] = producto
    print("Producto agregado con éxito.")

def ver_materiales():
    for material in materiales.values():
        print(f"Nombre: {material.nombre}, Código: {material.codigo}, Valor: {material.valor}, Cantidad: {material.cantidad}")

def ver_productos():
    for producto in productos.values():
        print(f"Nombre: {producto.nombre}, Código: {producto.codigo}, Valor total: {producto.calcular_valor()}")

def menu():
    while True:
        print("\nAdministrador de Materiales/Productos")
        print("1. Agregar Material")
        print("2. Agregar Producto")
        print("3. Ver Materiales")
        print("4. Ver Productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_material()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            ver_materiales()
        elif opcion == '4':
            ver_productos()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()
