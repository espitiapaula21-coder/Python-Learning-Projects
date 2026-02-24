# ==========================================
#      GESTOR DE TAREAS PROFESIONAL
# ==========================================

# 1. RECETA: La función para agregar (Nivel Básico)
def agregar_tarea(lista, nombre):
    lista.append(nombre)
    print(f"\n✅ Tarea '{nombre}' guardada con éxito.")

# 2. CAJA: Nuestra lista de datos (Nivel Intermedio)
mis_tareas = []

# 3. EL MOTOR: Bucle infinito para que el programa no se apague
while True:
    print("\n" + "="*30)
    print("      MENÚ DE CONTROL PRO")
    print("="*30)
    print("1. ➕ Agregar nueva tarea")
    print("2. 📋 Ver todas las tareas")
    print("3. 🗑️ Borrar una tarea")
    print("4. 🚪 Salir")
    
    # Escuchamos lo que el usuario quiere hacer
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        nueva = input("¿Qué tarea quieres guardar?: ")
        agregar_tarea(mis_tareas, nueva)
    
    elif opcion == "2":
        # Verificamos si la lista tiene elementos
        if len(mis_tareas) == 0:
            print("\n📭 La lista está vacía. ¡Agrega algo primero!")
        else:
            print("\n📋 TAREAS PENDIENTES:")
            # Usamos enumerate para que Python ponga los números 1, 2, 3...
            for i, t in enumerate(mis_tareas, 1):
                print(f"{i}. {t}")
            
    elif opcion == "3":
        if len(mis_tareas) == 0:
            print("\n📭 No hay nada que borrar.")
        else:
            # ESCUDO PROTECTOR (Try/Except) para evitar errores Pro
            try:
                print("\n¿Qué número de tarea quieres eliminar?")
                for i, t in enumerate(mis_tareas, 1):
                    print(f"{i}. {t}")
                
                # Convertimos el texto del usuario a número entero (int)
                indice = int(input("\nIntroduce el número: "))
                
                # Borramos usando pop (restamos 1 porque Python cuenta desde 0)
                tarea_eliminada = mis_tareas.pop(indice - 1)
                print(f"\n🗑️ Tarea '{tarea_eliminada}' eliminada.")
            
            except (ValueError, IndexError):
                # Si el usuario pone una letra o un número que no existe
                print("\n❌ ERROR: Debes poner un número válido de la lista.")

    elif opcion == "4":
        print("\n👋 ¡Gracias por usar el Gestor Pro! Éxito en tus estudios de ingeniería.")
        break # Rompemos el bucle y cerramos el programa
    
    else:
        print("\n❌ Opción no válida. Por favor, elige del 1 al 4.")
