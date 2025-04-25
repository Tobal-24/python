def mostrar_nivel(nombre, puntos):
    if puntos >= 1000:
        print(nombre, "está en el nivel PREMIUM (25% de descuento)")
    elif puntos >= 500:
        print(nombre, "está en el nivel ORO (10% de descuento)")
    elif puntos >= 250:
        print(nombre, "está en el nivel BRONCE (premios especiales)")
    else:
        print(nombre, "está en el nivel NORMAL (sin beneficios)")

# Datos de los clientes
mostrar_nivel("Marcos", 1500)
mostrar_nivel("Jose Luis", 2500)
mostrar_nivel("Sebastian", 300)

# Mensaje de despedida
print("¡Gracias por visitar Falabella!")
