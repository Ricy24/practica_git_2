# --- Calculadora de salud --


def calcular_IMC(peso, altura):
    pass
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros (ejemplo: 1.75): "))

imc = peso / (altura ** 2)

print(f"Tu IMC es: {round(imc, 2)}")

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    pass

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    pass

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    pass

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    pass

# --- Participacion usuario ---

nombre = input("Bienvenido, ¿cuál es tu nombre? ")
print("Hola", nombre, ", elige una opción:")
print("1. Calcular IMC")
print("2. Calcular Porcentaje de Grasa")
print("3. Calcular Calorías en Reposo (TMB)")
print("4. Calcular Calorías en Actividad")
print("5. Calcular Calorías para Adelgazar")

opcion = input("Escribe el número de la opción que quieres: ")

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))

if opcion == "1":
    resultado = calcular_IMC(peso, altura)
    print("Tu IMC es:", resultado)

elif opcion == "2":
    edad = int(input("Ingresa tu edad: "))
    genero = float(input("Ingresa 10.8 si eres hombre o 0 si eres mujer: "))
    resultado = calcular_porcentaje_grasa(peso, altura, edad, genero)
    print("Tu porcentaje de grasa es:", resultado, "%")

elif opcion == "3":
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Ingresa 5 si eres hombre o -161 si eres mujer: "))
    resultado = calcular_calorias_en_reposo(peso, altura, edad, genero)
    print("Tus calorías en reposo (TMB) son:", resultado)

elif opcion == "4":
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Ingresa 5 si eres hombre o -161 si eres mujer: "))
    print("Niveles de actividad: 1.2 (nula), 1.375 (ligera), 1.55 (moderada), 1.72 (deportista), 1.9 (atleta)")
    actividad = float(input("Ingresa el valor de tu actividad: "))
    resultado = calcular_calorias_en_actividad(peso, altura, edad, genero, actividad)
    print("Tus calorías diarias según tu actividad son:", resultado)

elif opcion == "5":
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Ingresa 5 si eres hombre o -161 si eres mujer: ")) 
    resultado = consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero)
    print(resultado)

else:
    print("Opción no válida. Por favor, reinicia el programa.")