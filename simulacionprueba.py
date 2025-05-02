def calcular_subsidio(quintil, condicion_laboral, edad):
    # Definir el subsidio base según el quintil y la condición laboral
    if quintil == 1:
        if condicion_laboral == "Desempleado":
            subsidio_base = 15000
        else:
            subsidio_base = 10000
    elif quintil == 2:
        if condicion_laboral == "Desempleado":
            subsidio_base = 8000
        else:
            subsidio_base = 6000
    elif quintil == 3:
        if condicion_laboral == "Desempleado":
            subsidio_base = 8000
        else:
            subsidio_base = 6000
    elif quintil == 4:
        if condicion_laboral == "Desempleado":
            subsidio_base = 8000
        else:
            subsidio_base = 6000
    else:  # Quintil 5
        subsidio_base = 1500

    # Bono adicional si el solicitante está en los quintiles 1 o 2
    bono_adicional = 0
    if quintil in [1, 2]:
        bono_adicional = 2000

    # Bono adicional si el solicitante tiene más de 65 años
    bono_extra_edad = 0
    if edad > 65:
        bono_extra_edad = 3000

    # Calcular el total del subsidio
    subsidio_total = subsidio_base + bono_adicional + bono_extra_edad
    
    return subsidio_total

# Solicitar datos al usuario
print("Por favor, ingresa los siguientes datos:")

quintil = int(input("Quintil de ingresos (1-5): "))
condicion_laboral = input("Condición laboral (Empleada/Desempleada): ").capitalize()
edad = int(input("Edad del solicitante: "))

# Calcular el subsidio
subsidio = calcular_subsidio(quintil, condicion_laboral, edad)

# Mostrar el resultado
print(f"El subsidio de gas que le corresponde es: ${subsidio}")













import random


# Paso 1: Ingreso del rango
minimo = int(input("Ingresa el número mínimo del rango: "))
maximo = int(input("Ingresa el número máximo del rango: "))


# Validación del rango
while minimo >= maximo:
    print("Error: el número mínimo debe ser menor que el máximo.")
    minimo = int(input("Ingresa el número mínimo del rango: "))
    maximo = int(input("Ingresa el número máximo del rango: "))


# Paso 2: Generar número aleatorio y ajustarlo
numero = random.randint(minimo, maximo)
numero_ajustado = round((numero / 4)) * 4


# Paso 3: Juego de adivinanza con 3 intentos
for intento in range(1, 4):
    adivina = int(input(f"Intento {intento}: Adivina el número: "))


    if adivina == numero_ajustado:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif intento < 3:
        if adivina < numero_ajustado:
            print("Pista: El número es mayor.")
        else:
            print("Pista: El número es menor.")
    else:
        print(f"¡Perdiste! El número correcto era {numero_ajustado}.")
             
