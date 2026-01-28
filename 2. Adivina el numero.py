import random # Traemos la herramienta para generar numeros aleatorios
numero_secreto = random. randint (1,100 ) # type: ignore
intentos = 0 # una caja para contar cuantas veces ha fallado
adivinado = False # empezamos diciendo que aun no has ganado
while adivinado == False:
    intento_usuario= int(input("Adivina el numero (1-100):")) # type: ignore
    intentos=intentos+1 # suma 1 al contador cada vez que el usuario escribe
    if intento_usuario<numero_secreto:
        print("¡Mas alto!")
    elif intento_usuario > numero_secreto:
        print("¡Mas bajo!")
    else:
        print(f"¡ FELICIDADES! Lo lograste en {intentos} intentos.")
        adivinado = True # Esto rompe el bucle y termina el programa


