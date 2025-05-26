#1 - se solicita desarrollar  un programa en Python que permita calcular el área de varios triángulos para esto se le solicita al usuario indicar cuantos triángulos desea procesar , 
#luego por cada triangulo se debe ingresar la base y la altura , ambos valores positivos irreales (es decir , pueden tener decimales). 

#l área de un triangulo se calcula de la siguiente forma : área =  base x altura dividido en 2 

#si su usuario ingresa un valor inválido se debe mostrar un mensaje de error 

cantidad_triangulos = int (input("cuantos triangulos desea procesar? "))


for i in range (cantidad_triangulos):
        
    try:

          base = float(input(f"ingrese la base del triangulo {i + 1}: "))

          altura = float (input(f"Ingrese la altura del triangulo {i + 1}: "))

        
          if base <= 0 or altura <= 0: 

           print( "Error , la base y la altura tienen que ser mayores a 0" )

    
          else:
    
           area = (base * altura) / 2

          print(f"El area del triangulo {i + 1} es : {area:.2f}")

    except ValueError:
    
       print("Error: Debes ingresar un número válido.")


            







 

