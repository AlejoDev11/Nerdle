from model.nerdle import Juego, Jugador, Dificultad

def mostrar_menu_dificultades(dificultades):
    print("Selecciona una dificultad:")
    for i, dificultad in enumerate(dificultades, start=1):
        print(f"{i}. {dificultad.nombre}")

def mostrar_mensaje_ganador():
    print("¡Felicidades, has ganado!")

def mostrar_mensaje_perdedor():
    print("¡Has perdido! Inténtalo de nuevo.")

def main():
    dificultades = [
        Dificultad("Fácil", ["90-45=45", "41+28=69", "37+59=96"]),
        Dificultad("Medio", ["9x6=54", "8x8=64", "71/0=0"]),
        Dificultad("Difícil", ["8x-21=3", "2(x+3)=12", "2x2+3x+5=0"])
    ]
    print("¡Bienvenido a Nerdle!")
    jugador_nombre = input("Ingresa tu nombre: ")
    jugador = Jugador(jugador_nombre)
    juego = Juego(jugador, dificultades)

    while True:
        mostrar_menu_dificultades(dificultades)
        opcion = input("Selecciona una opción (1-3): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 3:
                juego.seleccionar_dificultad(dificultades[opcion - 1].nombre)
                juego.iniciar_juego()

                while juego.jugador.intentos_disponibles > 0:
                    respuesta = input("Ingresa tu respuesta: ")
                    if juego.intentar_adivinar(respuesta):
                        mostrar_mensaje_ganador()
                        break
                    else:
                        print(f"Incorrecto. Te quedan {juego.jugador.intentos_disponibles} intentos.")
                        cambiar_dificultad = input("¿Quieres cambiar el nivel de dificultad? (s/n): ")
                        if cambiar_dificultad.lower() == 's':
                            break
                else:
                    mostrar_mensaje_perdedor()

                continuar = input("¿Quieres jugar de nuevo? (s/n): ")
                if continuar.lower() != 's':
                    break
            else:
                print("Opción no válida. Por favor, selecciona un número del 1 al 3.")
        else:
            print("Entrada inválida. Por favor, ingresa un número del 1 al 3.")

if __name__ == "__main__":
    main()
