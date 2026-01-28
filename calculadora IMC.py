# 1. Pedimos datos
peso = float(input("cuanto pesas en kg?: "))
altura = float(input("Cuanto mides en metros? (ej: 1.70): "))

# 2. Calculamos
imc = peso / (altura ** 2)

# 3. Clasificamos
if imc < 18.5:
    resultado = "Bajo peso"
elif imc < 25:
    resultado = "Peso normal"
elif imc < 30:
    resultado = "Sobrepeso"
else:
    resultado = "Obesidad"

# 4. MOSTRAMOS (Alineado a la izquierda)
print(f"Tu IMC es {imc:.2f}, lo que significa: {resultado}")


