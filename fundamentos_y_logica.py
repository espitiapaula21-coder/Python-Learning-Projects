# ==========================================================
# PORTAFOLIO DE FUNDAMENTOS Y LÓGICA EN PYTHON
# Desarrollado por: Paula Andrea
# ==========================================================

# --- SECCIÓN 1: OPERACIONES MATEMÁTICAS Y VARIABLES ---
# Cálculo de área de un rectángulo con valores estáticos y dinámicos
print("--- 1. Cálculo de Áreas ---")
base_fija = 10
altura_fija = 5
area_fija = base_fija * altura_fija
print(f"Área fija (10x5): {area_fija}")

# --- SECCIÓN 2: LÓGICA CONDICIONAL ---
# Validación de mayoría de edad y calificaciones
print("\n--- 2. Validaciones Condicionales ---")
edad = int(input("Ingresa tu edad para verificar: "))
if edad >= 18:
    print("Resultado: Mayor de edad")
else:
    print("Resultado: Menor de edad")

# Clasificación académica profesional
calificacion = int(input("Ingresa calificación (0-100): "))
if calificacion >= 90:
    print("Nivel: Excelente")
elif calificacion >= 80:
    print("Nivel: Bueno")
elif calificacion >= 70:
    print("Nivel: Suficiente")
else:
    print("Nivel: Necesitas mejorar")

# --- SECCIÓN 3: CONDICIONALES ANIDADOS ---
# Control de acceso con múltiples criterios
print("\n--- 3. Lógica de Acceso Anidada ---")
edad_evento = int(input("Edad para el evento: "))
if edad_evento >= 18:
    print("Acceso concedido")
else:
    permiso = input("¿Cuentas con permiso parental? (si/no): ").lower()
    if permiso == "si":
        print("Acceso concedido con autorización")
    else:
        print("Acceso denegado")

# --- SECCIÓN 4: ESTRUCTURAS DE REPETICIÓN (BUCLES) ---
# Iteraciones con For y While
print("\n--- 4. Demostración de Bucles ---")
# Uso de range
for n in range(1, 6):
    print(f"Iteración range: {n}")

# Clasificación de letras en una cadena
palabra_lab = "murcielago"
vocales = "aeiou"
for letra in palabra_lab:
    tipo = "vocal" if letra in vocales else "consonante"
    print(f"La letra '{letra}' es {tipo}")

# --- SECCIÓN 5: MINI-JUEGO DE LÓGICA ---
# Validación de intentos con bucle While
print("\n--- 5. Juego de Adivinanza ---")
numero_objetivo = 7
intento_usuario = 0
while intento_usuario != numero_objetivo:
    intento_usuario = int(input("Adivina el número secreto (1-10): "))
    if intento_usuario == numero_objetivo:
        print("¡Correcto! Has superado la prueba de lógica.")
    else:
        print("Sigue intentando...")
