# Datos del cliente
boleta = input("Número de Boleta: ")
id_cliente = input("Identificación del Cliente: ")
nombre = input("Nombre del Cliente: ")

# Lista de productos
productos = [
    "Perfume Organza", "Caty Perry", "Mañana Fresca", "La Mejor Noche", "Sueño Exclusivo",
    "Antonio Banderas", "Lacoste", "Hugo Boss", "¿A Qué Te Quitó el Sueño?", "Red"
]

total = 0

# Precios
precio_50ml = 10000
precio_100ml = 18000

# Ingreso de productos
for producto in productos:
    print(f"\nProducto: {producto}")
    cantidad = int(input("  Cantidad (0 si no compra): "))
    if cantidad > 0:
        ml = int(input("  Tamaño (50 o 100 ml): "))
        if ml == 50:
            total += cantidad * precio_50ml
        elif ml == 100:
            total += cantidad * precio_100ml

# Cálculos
iva = total * 0.19
subtotal = total - iva

# Resumen
print("\n--- RESUMEN ---")
print(f"Boleta: {boleta}")
print(f"Cliente: {nombre} | ID: {id_cliente}")
print(f"Subtotal: {subtotal} CLP")
print(f"IVA (19%): {iva} CLP")
print(f"Total a pagar: {total} CLP")