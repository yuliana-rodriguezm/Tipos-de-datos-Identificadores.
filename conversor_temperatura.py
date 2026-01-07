# Programa que convierte una temperatura de grados Celsius a Fahrenheit
# y muestra un mensaje según si la temperatura es fría o caliente.

# Pide el día del mes, uso el tipo de dato int
dia_mes = int(input("Ingrese el día del mes (1 al 31): "))
print("Día del mes:", dia_mes)

#Pide la temperatura, uso el tipo de dato float
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Identifica si hace frío o calor según la temperatura
# Uso el tipo de dato boolean
es_caliente = temperatura_celsius >= 25

# Muestra los resultados con el tipo de dato string
print("Temperatura ingresada:", temperatura_celsius, "°C")
print("Temperatura convertida:", temperatura_fahrenheit, "°F")

if es_caliente:
    print("El clima es caliente.")
else:
    print("El clima es frío.")
