def ejecutar_cajero():
    # --- CONFIGURACIÓN INICIAL ---
    saldo = 1000.0  # Variable numérica (float) para el dinero
    pin_secreto = "1234"  # Variable de texto (str) para seguridad
    abierto = True  # Booleano para controlar el bucle

    print("=== BIENVENIDO A PYTHON BANK ===")
    
    # Verificación de identidad inicial
    intento_pin = input("Ingrese su PIN de 4 dígitos: ")
    
    if intento_pin != pin_secreto:
        print("PIN Incorrecto. Acceso denegado.")
        return # Finaliza la función aquí mismo

    # --- BUCLE PRINCIPAL (El programa vive aquí) ---
    while abierto:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        # --- LÓGICA DE DECISIÓN (Condicionales) ---
        if opcion == "1":
            print(f"Su saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            monto = float(input("Monto a depositar: $"))
            if monto > 0:
                saldo += monto  # Sumamos al saldo: saldo = saldo + monto
                print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("Error: El monto debe ser positivo.")

        elif opcion == "3":
            monto = float(input("Monto a retirar: $"))
            if monto > saldo:
                print("⚠️ Fondos insuficientes.")
            elif monto <= 0:
                print("Error: Monto no válido.")
            else:
                saldo -= monto  # Restamos al saldo: saldo = saldo - monto
                print(f"Retiro exitoso. Saldo restante: ${saldo:.2f}")

        elif opcion == "4":
            print("Cerrando sesión... Gracias por confiar en nosotros.")
            abierto = False # Rompemos la condición del 'while' para salir
        
        else:
            print("Opción no válida. Intente de nuevo.")

# --- EJECUCIÓN ---
ejecutar_cajero()
