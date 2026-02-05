peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros (ejemplo: 1.75): "))

imc = peso / (altura ** 2)

print(f"Tu IMC es: {round(imc, 2)}")