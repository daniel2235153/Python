#Diseñe un algoritmo que permita jugar piedra, papel y tijera. Su programa debe tener dos modos:
#  jugar contra el pc o multijugador(dos jugadores). Tenga en cuenta que pueden existir empates. 
# Su programa debe solicitar el ID del jugador y permitir varias rondas hasta que no se desee jugar más, 
# así mismo debe llevar un contador de puntos para al finalizar la partida decir quien es el ganador. 
import random

print("¡Bienvenido a Piedra, Papel o Tijera!")
print("Elige un modo de juego:")
print("1. Contra el PC")
print("2. Multijugador")

modo = input("Selecciona el modo (1 o 2): ")
if modo not in ['1', '2']:
    print("Modo no válido.")
else:
    jugador1_id = input("Ingresa el ID del jugador 1: ")
    if modo == '2':
        jugador2_id = input("Ingresa el ID del jugador 2: ")
    else:
        jugador2_id = "PC"

    puntos_jugador1 = 0
    puntos_jugador2 = 0
    ronda = 1

    while True:
        print(f"\n--- Ronda {ronda} ---")
        print(f"{jugador1_id}, elige tu jugada:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        jugada1 = input("Ingresa el número de tu jugada: ")

        if jugada1 not in ['1', '2', '3']:
            print("Jugada no válida. Pierdes esta ronda.")
            puntos_jugador2 += 1
        else:
            if modo == '2':
                print(f"{jugador2_id}, elige tu jugada:")
                print("1. Piedra")
                print("2. Papel")
                print("3. Tijera")
                jugada2 = input("Ingresa el número de tu jugada: ")

                if jugada2 not in ['1', '2', '3']:
                    print("Jugada no válida. Pierdes esta ronda.")
                    puntos_jugador1 += 1
                    jugada2 = None
            else:
                jugada2 = str(random.randint(1, 3))
                opciones = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
                print(f"El PC elige: {opciones[jugada2]}")

            if jugada2:
                # Decidir el ganador de la ronda
                if jugada1 == jugada2:
                    print("¡Empate!")
                elif (jugada1 == '1' and jugada2 == '3') or (jugada1 == '2' and jugada2 == '1') or (jugada1 == '3' and jugada2 == '2'):
                    print(f"¡{jugador1_id} gana la ronda!")
                    puntos_jugador1 += 1
                else:
                    print(f"¡{jugador2_id} gana la ronda!")
                    puntos_jugador2 += 1

        print(f"Puntos actuales: {jugador1_id} ({puntos_jugador1}) - {jugador2_id} ({puntos_jugador2})")
        ronda += 1

        continuar = input("\n¿Desean jugar otra ronda? (s/n): ").lower()
        if continuar != 's':
            break

    print("\n--- Resultado final ---")
    print(f"{jugador1_id}: {puntos_jugador1} puntos")
    print(f"{jugador2_id}: {puntos_jugador2} puntos")
    if puntos_jugador1 > puntos_jugador2:
        print(f"¡{jugador1_id} es el ganador!")
    elif puntos_jugador2 > puntos_jugador1:
        print(f"¡{jugador2_id} es el ganador!")
    else:
        print("¡Es un empate!")
