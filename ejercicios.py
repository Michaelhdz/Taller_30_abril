import math

# Ejercicio 1
nombre = str(input("Ingrese su nombre: "))
adjetivo_calificativo = str(input("Ingrese un adjetivo calificativo para su nombre: "))
print(nombre, adjetivo_calificativo)

# Ejercicio 2
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
print("La suma de los números es: ", numero1 + numero2)

# Ejercicio 3
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
print("La suma de los números es: ", numero1 + numero2)
print("La resta de los números es: ", numero1 - numero2)
print("La multiplicacion de los números es: ", numero2 * numero2)
print("La division de los números es: ", numero1 / numero2)
print("El residuo de los números es: ", numero1 % numero2)

# Ejercicio 4
numero = float(input("Ingrese un numero decimal: "))
parte_entera = int(numero)
parte_decimal = numero - parte_entera
print("la parte entera es: ", parte_entera, "y la parte decimal es: ", parte_decimal)

# Ejercicio 5
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))
print("La nota final es: ", nota1 * 0.15 + nota2 * 0.20 + nota3 * 0.15 + nota4 * 0.30 + nota5 * 0.20)

# Ejercicio 6
venta = int(input("Ingrese el valor de la venta: "))
iva = venta * 0.19
print("El valor de la venta es: ", venta, "El valor del IVA es: ", iva,
      "El valor de la venta más IVA es: ", venta + (venta * 0.19))

# Ejercicio 7
radio = float(input("Ingrese el radio del círculo: "))
print("El area del círculo es ", 3.14159 * (radio ** 2), "y el perimetro del círculo es ", 2 * 3.14159 * radio)

# Ejercicio 8
lado = float(input("Ingrese la longitud de un lado del hexágono: "))
apotema = float(input("Ingrese la longitud de la apotema del hexágono: "))
print("El área del hexágono es: ", ((lado * 6) * apotema) / 2)

# Ejercicio 9
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
print("El promedio de los tres números es: ", (numero1 + numero2 + numero3) / 3)

# Ejercicio 10
variable1 = int(input("Ingrese un número entero: "))
variable2 = int(input("Ingrese otro número: "))
print("Los valores iniciales son: a =", variable1, "y b =", variable2)
cambio1 = variable2
cambio2 = variable1
print("Los valores intercambiados son a =", cambio1, "y b =", cambio2)

# Ejercicio 11
altura = float(input("Ingrese la altura a la que será lanzado el objeto (en metros): "))
print("El tiempo de caída del objeto es de", math.sqrt((2 * altura) / 10), "segundos")

# ejercicio 12
velocidad = int(input("ingrese la velocidad (en metros por segundo) a la que se mueve el objeto: "))
aceleracion = int(input("ingrese la aceleración (en metros por segundo al cuadrado) del objeto: "))
tiempo = int(input("ingrese el tiempo (en segundos) con el que desea calcular la distancia recorrida por el objeto: "))
distancia = ((velocidad * tiempo) + (0.5 * (aceleracion * (tiempo ** 2))))
print("la distancia recorrida por el objeto es de: ", distancia, "metros")

# Ejercicio 14
masa = float(input("Ingrese la masa del objeto (en kilogramos): "))
velocidad_de_la_luz = 299792458
print("La energía del objeto es de", masa * velocidad_de_la_luz ** 2, "Julios")

# Ejercicio 15
coordenada_x1 = float(input("Digite la coordenada x1: "))
coordenada_y1 = float(input("Digite la coordenada x2: "))
coordenada_x2 = float(input("Digite la coordenada y1: "))
coordenada_y2 = float(input("Digite la coordenada y2: "))
print("La distancia entre los puntos es de", math.sqrt((coordenada_x2 - coordenada_x1)**2 + (coordenada_y2 - coordenada_y1)**2))

# Ejercicio 16
segundos = int(input("Ingrese los segundos a transformar: "))
print(segundos, "segundos equivalen a", segundos / 3600, "horas")

# Ejercicio 17
segundos = int(input("Ingrese los segundos a transformar: "))
print(segundos, "segundos equivalen a", segundos / 60, "minutos")

# Ejercicio 18
segundos = int(input("Ingrese un tiempo en segundos: "))
hora = segundos / 3600
segundos = segundos % 3600
minutos = segundos / 60
segundos = segundos % 60
print("la hora es:", int(hora), int(minutos), segundos)

# Ejercicio 19
dinero = int(input("Ingrese una cantidad de dinero: "))
mil = round(dinero / 1000)
dos_mil = round(dinero / 2000)
cinco_mil = round(dinero / 5000)
diez_mil = round(dinero / 10000)
veinte_mil = round(dinero / 20000)
cincuenta_mil = round(dinero / 50000)
cien_mil = round(dinero / 100000)

if mil < 1:
    print("No tiene billetes de mil")
else:
    print("la cantida minima de billetes de billetes de mil es de:", mil)
if dos_mil < 1:
    print("No tiene billetes de dos mil")
else:
    print("la cantida minima de billetes de billetes de dos mil es de:", dos_mil)
if cinco_mil < 1:
    print("No tiene billetes de cinco mil")
else:
    print("la cantida minima de billetes de billetes de cinco mil es de:", cinco_mil)
if diez_mil < 1:
    print("No tiene billetes de diez mil")
else:
    print("la cantida minima de billetes de billetes de diez mil es de:", diez_mil)
if veinte_mil < 1:
    print("No tiene billetes de veinte mil")
else:
    print("la cantida minima de billetes de billetes de veinte mil es de:", veinte_mil)
if cincuenta_mil < 1:
    print("No tiene billetes de cincuenta mil")
else:
    print("la cantida minima de billetes de billetes de cincuenta mil es de:", cincuenta_mil)
if cien_mil < 1:
    print("No tiene billetes de cien mil")
else:
    print("la cantida minima de billetes de billetes de cien mil es de:", cien_mil)

# Ejercicio 20


def invertir(numero):
    invertido = ""
    for n in numero:
        invertido = n + invertido
    return invertido


numero = str(input("Ingrese un número entero a invertir: "))
print(invertir(numero))

# Ejercicio 21
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejercicio 22
numero = int(input("ingrese un número entero: "))
if numero < 0:
    print("el número es negativo")
elif numero == 0:
    print("el número es neutro")
else:
    print("el número es positivo")

# Ejercicio 23
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    if numero > 0:
        print("El número es par positivo.")
    else:
        print("El número es par negativo.")
else:
    if numero > 0:
        print("El número es impar positivo.")
    else:
        print("El número es impar negativo.")

# Ejercicio 24
venta = int(input("Ingrese el valor de la venta: "))
iva = venta * 0.19
descuento = venta * 0.05
if venta >= 150000:
    print("El valor de la venta mas iva y con descuento es de", (venta + iva) - descuento)
else:
    print("El valor de la venta mas iva es de", venta + iva)

# Ejercicio 25
numero = int(input("Ingrese un número: "))
if numero >= 10:
    print("el triple del número es", numero * 3)
else:
    print("La cuarta parte del número es: ", numero / 4)

# Ejercicio 26
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))
nota_final = (nota1 * 0.15) + (nota2 * 0.20) + (nota3 * 0.15) + (nota4 * 0.30) + (nota5 * 0.20)
if nota_final < 2.0:
    print("No puede habilitar.")
if nota_final < 3.0:
    print("Reprobó.")
if nota_final >= 3.0:
    print("Aprobó.")
if nota_final > 4.5:
    print("Felicitaciones.")

# Ejercicio 27
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
print("El número mayor es", max(numero1, numero2))

# Ejercicio 28
numero = int(input("Ingrese un número entero: "))
print("El número ingresado equivale a", float(numero), "en decimal.")

# Ejercicio 29
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el ultimo número: "))
print("El número mayor es", max(numero1, numero2, numero3), "y el menor es", min(numero1, numero2, numero3))

# Ejercicio 30
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
suma = numero1 + numero2
if suma > numero3:
    print("La suma de los dos primeros números es mayor que el tercer número ingresado.")
else:
    print("La suma de los dos primeros números es menor que el tercer número ingresado.")

# Ejercicio 31
distancia = int(input("Ingrese la distancia a recorrer (en kilómetros): "))
dias = int(input("Ingrese los días de estancia: "))
pasaje = 5000 * distancia
if distancia > 1000 and dias > 7:
    print(pasaje - (pasaje * 0.15))
else:
    print("El precio del pasaje es", pasaje)

# Ejercicio 32
year = int(input("Ingrese un año: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

# Ejercicio 34
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")
usuario_predefinido = "admin"
contrasena_predefinida = "admin"
if usuario == usuario_predefinido and contrasena == contrasena_predefinida:
    print("Inicio de sesión completado")
else:
    print("Inicio de sesión fallido (usuario o contraseña incorrectos).")

# Ejercicio 35
numero = int(input("Ingrese un número del 0 al 10: "))
if numero == 0:
    print("CERO")
elif numero == 1:
    print("UNO")
elif numero == 2:
    print("DOS")
elif numero == 3:
    print("TRES")
elif numero == 4:
    print("CUATRO")
elif numero == 5:
    print("CINCO")
elif numero == 6:
    print("SEIS")
elif numero == 7:
    print("SIETE")
elif numero == 8:
    print("OCHO")
elif numero == 9:
    print("NUEVE")
elif numero == 10:
    print("DIEZ")
else:
    print("ERROR (El número no está entre 0 y 10.")

# Ejercicio 36
numero = int(input("Ingrese un número menor a 100000: "))
if numero < 100000:
    print("El número", "(", numero, ")", "tiene", len(str(numero)), "dígitos")
else:
    print("ERROR (el número es mayor a 100000)")

# Ejercicio 37
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
if numero1 < numero2 < numero3:
    print("Los números se incrementan.")
elif numero1 > numero2 > numero3:
    print("Los números disminuyen.")
else:
    print("Los números no se incrementan ni se disminuyen")

# Ejercicio 38
numero1 = int(input("ingrese el primer número: "))
numero2 = int(input("ingrese el segundo número: "))
if 0 <= numero1 < 6 and 0 <= numero2 < 6:
    print("True")
else:
    print("False")

# Ejercicio 39
dia = int(input("Ingrese el número de algún día de la semana (1 a 7): "))
if dia == 1:
    print("El día es lunes.")
elif dia == 2:
    print("El día es martes.")
elif dia == 3:
    print("El día es miércoles.")
elif dia == 4:
    print("El día es jueves.")
elif dia == 5:
    print("El día es viernes.")
elif dia == 6:
    print("El día es sábado.")
elif dia == 7:
    print("El día es domingo.")
else:
    print("ERROR (ingresó un número que no está entre 1 y 7).")

# Ejercicio 40
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Al menos dos de los números son iguales.")
else:
    print("No hay números iguales.")

# Ejercicio 41
print("Los diez primeros números naturales son:")
for x in range(0, 10):  # algunos cuentan los numeros naturales desde 0 y otros desde 1
    print(x, "", end="")

# Ejercicio 42
print("Los diez primeros números naturales impares son:")
for x in range(1, 20, 2):
    print(x)

# Ejercicio 43
print("Los diez primeros números naturales pares son:")
for x in range(2, 21, 2):
    print(x)

# Ejercicio 45
numero = int(input("Ingrese un número entero: "))
for x in range(numero):
    print(-x + 1 - 2)

# Ejercicio 46
numero = int(input("Ingrese el primer número: "))
numero_mayor = int(input("Ingrese un número mayor al primer número: "))
for x in range(numero, numero_mayor + 1):
    if numero_mayor > numero:
        print(x, "", end="")
    else:
        print("Error. El segundo número es menor o igual que el primero")

# Ejercicio 47
numero = int(input("Ingrese el primer número: "))
numero_mayor = int(input("Ingrese un número mayor al primer número: "))
if numero_mayor > numero:
    print(sum(range(numero, numero_mayor + 1)))
else:
    print("Error. El segundo número es menor o igual que el primero")

# Ejercicio 48
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))
numero4 = int(input("Ingrese otro número: "))
numero5 = int(input("Ingrese otro número: "))
numero6 = int(input("Ingrese otro número: "))
numero7 = int(input("Ingrese otro número: "))
numero8 = int(input("Ingrese otro número: "))
numero9 = int(input("Ingrese otro número: "))
numero10 = int(input("Ingrese otro número: "))
print("La suma de los números ingresados es:", numero1 + numero2 + numero3 + numero4 + numero5 + numero6 + numero7 + numero8 + numero9 + numero10)
print("El promedio de los números ingresados es:", (numero1 + numero2 + numero3 + numero4 + numero5 + numero6 + numero7 + numero8 + numero9 + numero10) / 10)

# Ejercicio 49
contador = 0
sumatoria = 0
numero = 1
while numero != 0:
    numero = int(input("Ingrese un número entero (0 para parar la cuenta y obtener resultados): "))
    if numero != 0:
        sumatoria += numero
        contador += 1
print("La sumatoria de los números ingresados es:", sumatoria)
print("El promedio de los números ingresados es: ", sumatoria / contador)

# Ejercicio 57
print(1)
print(1, 2)
print(1, 2, 3)
print(1, 2, 3, 4)
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, 6)
print(1, 2, 3, 4, 5, 6, 7)
print(1, 2, 3, 4, 5, 6, 7, 8)
print(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
