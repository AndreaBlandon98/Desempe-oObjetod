
import mysql.connector

# Conéctate a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_base_de_datos"
)

mycursor = mydb.cursor()

# Crea la tabla de productos
mycursor.execute(
    "CREATE TABLE productos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), cantidad INT, precio FLOAT)")


# Función para agregar un producto
def agregar_producto(nombre, cantidad, precio):
    sql = "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
    val = (nombre, cantidad, precio)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Producto agregado correctamente")


# Función para consultar todos los productos
def consultar_productos():
    mycursor.execute("SELECT * FROM productos")
    result = mycursor.fetchall()
    for producto in result:
        print(producto)


# Función para actualizar la información de un producto
def actualizar_producto(id, nombre, cantidad, precio):
    sql = "UPDATE productos SET nombre = %s, cantidad = %s, precio = %s WHERE id = %s"
    val = (nombre, cantidad, precio, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Producto actualizado correctamente")


# Función para eliminar un producto
def eliminar_producto(id):
    sql = "DELETE FROM productos WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Producto eliminado correctamente")


# Menú interactivo
while True:
    print("\n1. Agregar producto\n2. Consultar productos\n3. Actualizar producto\n4. Eliminar producto\n5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        agregar_producto(nombre, cantidad, precio)

    elif opcion == "2":
        consultar_productos()

    elif opcion == "3":
        id = int(input("Ingrese el ID del producto a actualizar: "))
        nombre = input("Ingrese el nuevo nombre: ")
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        actualizar_producto(id, nombre, cantidad, precio)

    elif opcion == "4":
        id = int(input("Ingrese el ID del producto a eliminar: "))
        eliminar_producto(id)

    elif opcion == "5":
        break

