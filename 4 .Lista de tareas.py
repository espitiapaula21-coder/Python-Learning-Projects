# 1. Preparamos la lista vacía y la variable de control
mis_tareas = [] 
continuar = True 

print("--- MI LISTA DE TAREAS ---")
while continuar: 
    # Mostramos el menú de opciones
    print("\nMENÚ DE OPCIONES:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Borrar una tarea")
    print("4. Cuántas tareas tengo")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ") 
    
    if opcion == "1":
        nueva = input("¿Qué tarea quieres agregar?: ")
        mis_tareas.append(nueva) # Agregamos a la lista 
        print("¡Tarea guardada con éxito!")
        
    elif opcion == "2":
        print("\nTUS TAREAS PENDIENTES:")
        if len(mis_tareas) == 0:
            print("La lista está vacía.")
        else:
            print(mis_tareas) # Mostramos la lista completa [cite: 2025-12-29]
        
    elif opcion == "3":
        # Primero revisamos si hay algo que borrar
        if len(mis_tareas) > 0:
            borrar = input("Escribe el nombre EXACTO de la tarea a borrar: ")
            if borrar in mis_tareas:
                mis_tareas.remove(borrar) # Quitamos de la lista [cite: 2025-12-29]
                print(f"¡'{borrar}' eliminada!")
            else:
                print("Esa tarea no existe en la lista.")
        else:
            print("No hay nada que borrar, la lista está vacía.")

    elif opcion == "4":
        # Usamos len() para contar
        cantidad = len(mis_tareas) 
        print(f"Tienes {cantidad} tareas en tu lista.")
        
    elif opcion == "5":
        print("¡Saliendo del programa... Adiós!")
        continuar = False # Rompemos el bucle
