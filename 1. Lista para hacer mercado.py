# 1. Definimos los precios en números enteros [cite: 2025-12-29]
inventario = {
    "leche": 3500,
    "pan": 2000,
    "huevos": 18000,
    "carne": 25000,
    "arroz": 4500
}

# 2. Configuración inicial [cite: 2025-12-29]
presupuesto = 200000
carrito = []
print(f"Presupuesto inicial: ${presupuesto:,}")

continuar = True
while continuar:
    print("\n--- PRODUCTOS EN PESOS ---")
    for producto, precio in inventario.items():
        print(f"- {producto.capitalize()}: ${precio:,}")

    seleccion = input("\n¿Qué quieres comprar? (o 'salir'): ").lower()

    if seleccion == "salir":
        continuar = False
    if seleccion == "0":
        # Debes poner estas líneas para agregar productos
        nuevo_p = input("Nombre del nuevo producto: ").lower()
        nuevo_precio = int(input(f"Precio para {nuevo_p}: "))
        inventario[nuevo_p] = nuevo_precio 
        print(f"✅ {nuevo_p} agregado.")
    elif seleccion == "8":
        producto_borrar = input("¿Qué producto deseas eliminar de la tienda?: ").lower()
        
        if producto_borrar in inventario:
            del inventario[producto_borrar] # Eliminamos del diccionario [cite: 2025-12-29]
            print(f"🗑️ El producto '{producto_borrar}' ha sido eliminado del inventario.")
        else:
            print("⚠️ Ese producto no existe en la tienda.")
        nuevo_p = input("Nombre del nuevo producto: ").lower()
        nuevo_precio = int(input(f"Precio para {nuevo_p}: "))
        inventario[nuevo_p] = nuevo_precio # Agregamos al diccionario 
        print(f"✅ {nuevo_p} ahora está disponible en la tienda.")
    elif seleccion in inventario:
        precio_p = inventario[seleccion]
        
        # Preguntamos la cantidad 
        try:
            cantidad = int(input(f"¿Cuántas unidades de {seleccion} quieres?: "))
            costo_total = precio_p * cantidad # Operador de multiplicación 
            
            # Verificamos presupuesto 
            if presupuesto >= costo_total:
                presupuesto -= costo_total # Restamos el dinero 
                
                # Agregamos a la lista 
                for i in range(cantidad):
                    carrito.append(seleccion)
                    
                print(f"✅ Agregaste {cantidad} {seleccion}(s). Costo: ${costo_total:,}")
                print(f"💰 Saldo restante: ${presupuesto:,}")
            else:
                print(f"❌ No te alcanza. {cantidad} unidades cuestan ${costo_total:,}")
        except ValueError:
            print("⚠️ Por favor, ingresa un número válido para la cantidad.")
            
    else:
        print("⚠️ Producto no encontrado.")

# Resumen final usando la lista acumulada 
print("\n" + "="*30)
print("RESUMEN DE TU COMPRA")
print(f"Carrito final: {carrito}")
print(f"Te sobraron: ${presupuesto:,}")
print("="*30)
print("\n" + "="*35)
print("       FACTURA DE VENTA")
print("="*35)

# Usamos set() para obtener los productos sin repetir y contarlos 
total_final = 0
for item in set(carrito):
    unidades = carrito.count(item)
    precio_unitario = inventario[item]
    subtotal = unidades * precio_unitario
    total_final += subtotal
    print(f"{item.capitalize():<10} x{unidades} ... ${subtotal:,}")

print("-" * 35)
print(f"TOTAL A PAGAR:      ${total_final:,}")
print(f"SALDO EN CUENTA:    ${presupuesto:,}")
print("="*35)
print("   ¡Gracias por su compra!")
# --- GUARDAR EN ARCHIVO [.txt] --- 
try:
    with open("factura_mercado.txt", "w", encoding="utf-8") as archivo:
        archivo.write("======= FACTURA GENERADA =======\n")
        for item in set(carrito):
            unidades = carrito.count(item)
            archivo.write(f"{item.capitalize()}: {unidades} unidades\n")
        
        archivo.write("--------------------------------\n")
        archivo.write(f"TOTAL GASTADO: ${200000 - presupuesto:,}\n")
        archivo.write(f"SALDO RESTANTE: ${presupuesto:,}\n")
        archivo.write("================================\n")
    print("\n💾 ¡Factura guardada con éxito en 'factura_mercado.txt'!")
except Exception as e:
    print(f"No se pudo guardar el archivo: {e}")
