nombre = input("Ingresa tu nombre: ")
calificacion = float(input("Ingresa tu calificación: "))

print("Bienvenid@!", nombre)
print("Tu calificación es:", calificacion)

if calificacion > 6.0:
    print("Has ganado un 20% de descuento.")
elif calificacion > 5.0:
    print("Has ganado un 15% de descuento.")
elif calificacion > 4.0:
    print("Has ganado un 10% de descuento.")
else:
    print("Te invitamos a seguir participando.")


