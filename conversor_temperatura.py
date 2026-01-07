# Programa que convierte una temperatura de grados Celsius a Fahrenheit
# y muestra un mensaje según si la temperatura es fría o caliente.

# Pide el día del mes, uso el tipo de dato int
dia_mes = int(input("Ingrese el día del mes (1 al 31): "))
print("Día del mes:", dia_mes)

#Pide la temperatura, usando el tipo de dato float
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Transforma la temperatura de grados Celcius a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Identifica si hace frío o calor según la temperatura
# Uso del tipo de dato boolean
es_caliente = temperatura_celsius >= 25
print("¿Es caliente?:", es_caliente)

# Muestra los resultados con el tipo de dato string
print("Temperatura ingresada en celcius:", temperatura_celsius, "°C")
print("Temperatura convertida a Fahrenheit:", temperatura_fahrenheit, "°F")

if es_caliente:
    print("El clima es caliente.")
else:
    print("El clima es frío.")
