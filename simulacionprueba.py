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
             
