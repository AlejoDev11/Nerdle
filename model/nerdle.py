import random

class Operacion:
    def __init__(self, operacion_str):
        self.operacion = operacion_str

    def verificar_respuesta(self, respuesta):
        return self.operacion == respuesta


class Dificultad:
    def __init__(self, nombre, operaciones):
        self.nombre = nombre
        self.operaciones = [Operacion(op) for op in operaciones]

    def obtener_operacion_aleatoria(self):
        return random.choice(self.operaciones)


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intentos_disponibles = 0

    def decrementar_intentos(self):
        self.intentos_disponibles -= 1


class Juego:
    def __init__(self, jugador, dificultades):
        self.jugador = jugador
        self.dificultades = dificultades
        self.dificultad_actual = None
        self.operacion_actual = None

    def seleccionar_dificultad(self, nombre_dificultad):
        for dificultad in self.dificultades:
            if dificultad.nombre == nombre_dificultad:
                self.dificultad_actual = dificultad
                self.jugador.intentos_disponibles = len(dificultad.operaciones)
                break

    def iniciar_juego(self):
        if self.dificultad_actual is None:
            raise ValueError("¡Primero selecciona una dificultad!")
        self.operacion_actual = self.dificultad_actual.obtener_operacion_aleatoria()

    def intentar_adivinar(self, respuesta):
        if self.operacion_actual.verificar_respuesta(respuesta):
            return True
        else:
            self.jugador.decrementar_intentos()
            return False
