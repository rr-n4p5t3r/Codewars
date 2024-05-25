import random

class RubiksCube:
    def __init__(self):
        # Inicializar cada cara del cubo con un color diferente
        self.caras = {
            'B': ['B'] * 9,  # Blanco
            'A': ['A'] * 9,  # Amarillo
            'U': ['U'] * 9,  # Azul
            'V': ['V'] * 9,  # Verde
            'R': ['R'] * 9,  # Rojo
            'N': ['N'] * 9   # Naranja
        }

    def print_cubo(self):
        # Imprimir el estado actual del cubo
        for color, cara in self.caras.items():
            print(f"Cara {color}:")
            for i in range(0, 9, 3):
                print(cara[i:i+3])
            print()

    def rotate_cara_horario(self, color):
        # Rotar la cara en sentido horario
        cara = self.caras[color]
        nueva_cara = [
            cara[6], cara[3], cara[0],
            cara[7], cara[4], cara[1],
            cara[8], cara[5], cara[2]
        ]
        self.caras[color] = nueva_cara

        # Actualizar las caras adyacentes
        self._rotate_adjacent_faces_clockwise(color)

    def rotate_cara_antihorario(self, color):
        # Rotar una cara tres veces en sentido horario es equivalente a rotar una vez en sentido antihorario
        self.rotate_cara_horario(color)
        self.rotate_cara_horario(color)
        self.rotate_cara_horario(color)

    def _rotate_adjacent_faces_clockwise(self, color):
        # Diccionario para almacenar las caras adyacentes y las posiciones de los elementos a intercambiar
        adjacent = {
            'B': [('U', [0, 1, 2]), ('R', [0, 1, 2]), ('V', [0, 1, 2]), ('N', [0, 1, 2])],
            'A': [('U', [6, 7, 8]), ('N', [6, 7, 8]), ('V', [6, 7, 8]), ('R', [6, 7, 8])],
            'U': [('B', [0, 3, 6]), ('N', [6, 3, 0]), ('A', [8, 5, 2]), ('R', [2, 5, 8])],
            'V': [('B', [8, 5, 2]), ('R', [6, 3, 0]), ('A', [0, 3, 6]), ('N', [2, 5, 8])],
            'R': [('B', [2, 5, 8]), ('U', [2, 5, 8]), ('A', [2, 5, 8]), ('V', [2, 5, 8])],
            'N': [('B', [0, 3, 6]), ('V', [2, 1, 0]), ('A', [8, 7, 6]), ('U', [6, 7, 8])]
        }

        if color not in adjacent:
            raise ValueError(f"Color {color} no válido")

        # Guardar los valores antes de rotar
        temp = [self.caras[adj[0]][adj[1][i]] for adj in adjacent[color] for i in range(3)]

        # Rotar las caras adyacentes
        for i in range(4):
            next_face, next_pos = adjacent[color][i]
            for j in range(3):
                self.caras[next_face][next_pos[j]] = temp[(i * 3 + j - 3) % 12]

    def desordenar(self, movimientos=20):
        caras = list(self.caras.keys())
        for _ in range(movimientos):
            cara = random.choice(caras)
            sentido = random.choice(['horario', 'antihorario'])
            if sentido == 'horario':
                self.rotate_cara_horario(cara)
            else:
                self.rotate_cara_antihorario(cara)

if __name__ == "__main__":
    cube = RubiksCube()
    cube.desordenar()
    cube.print_cubo()

    while True:
        comando = input("Ingrese el movimiento (e.g., 'B horario' o 'R antihorario') o 'salir' para terminar: ")
        if comando.lower() == 'salir':
            break
        try:
            color, sentido = comando.split()
            if sentido == 'horario':
                cube.rotate_cara_horario(color.upper())
            elif sentido == 'antihorario':
                cube.rotate_cara_antihorario(color.upper())
            else:
                print("Sentido no válido. Use 'horario' o 'antihorario'.")
        except ValueError:
            print("Entrada no válida. Use el formato 'Color Sentido'.")

        cube.print_cubo()
