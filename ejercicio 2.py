productos = {
    "Jabon de bañar": 85.0,
    "Rinso": 1.0,
    "Pasta de Diente": 1.0,
    "Legia": 1.25,
    "Jabon de Traste": 1.50,
    
 

}

nombre_producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))


if nombre_producto in productos:
    precio_unitario = productos[nombre_producto]
    total_pagar = precio_unitario * cantidad
    print(f"El total a pagar por {cantidad} {nombre_producto} es: ${total_pagar}")
else:
    print("El producto no se encuentra disponible en el inventario.")
