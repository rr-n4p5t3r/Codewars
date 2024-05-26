import random
import time

class Vehiculo:
    """
    Clase que representa un vehículo en la autopista.
    """
    def __init__(self, id):
        """
        Inicializa un vehículo con un ID único, una posición inicial en 0
        y un carril aleatorio entre 0 y 7.
        """
        self.id = id
        self.posicion = 0
        self.carril = random.randint(0, 7)

    def mover(self):
        """
        Mueve el vehículo una posición hacia adelante en la autopista.
        """
        self.posicion += 1

    def __str__(self):
        """
        Devuelve una representación en cadena del vehículo en formato 'Vehiculo ID en carril CARRIL en posicion POSICION'.
        """
        return f"Vehiculo {self.id} en carril {self.carril} en posicion {self.posicion}"

class Semafaro:
    """
    Clase que representa un semáforo en la autopista.
    """
    def __init__(self):
        """
        Inicializa un semáforo en estado verde por defecto.
        """
        self.estado = 'verde'

    def cambiar_estado(self):
        """
        Cambia el estado del semáforo de verde a rojo, o viceversa.
        """
        self.estado = 'rojo' if self.estado == 'verde' else 'verde'

    def __str__(self):
        """
        Devuelve una representación en cadena del semáforo y su estado actual.
        """
        return f"El semafaro esta {self.estado}"

class Autopista:
    """
    Clase que representa una autopista con vehículos y semáforos.
    """
    def __init__(self):
        """
        Inicializa una autopista sin vehículos y con 8 semáforos.
        """
        self.vehiculos = []
        self.semafaro = [Semafaro() for _ in range(8)]

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo a la autopista.
        """
        self.vehiculos.append(vehiculo)

    def mover_vehiculos(self):
        """
        Mueve todos los vehículos en la autopista una posición hacia adelante.
        """
        for vehiculo in self.vehiculos:
            vehiculo.mover()

    def revisar_colisiones(self):
        """
        Revisa si hay colisiones entre los vehículos en la autopista.
        """
        posiciones = {}
        for vehiculo in self.vehiculos:
            if (vehiculo.carril, vehiculo.posicion) in posiciones:
                print(f"Colision detectada en carril {vehiculo.carril} posicion {vehiculo.posicion}")
            posiciones[(vehiculo.carril, vehiculo.posicion)] = vehiculo.id

    def mostrar(self):
        """
        Muestra el estado actual de la autopista, incluyendo semáforos y vehículos en cada carril.
        """
        for i, semafaro in enumerate(self.semafaro):
            print(f"Carril {i}: {semafaro} -", end=" ")
            for vehiculo in self.vehiculos:
                if vehiculo.carril == i:
                    print(f"{vehiculo}", end=" ")
            print()

# Crear una instancia de la autopista
autopista = Autopista()

# Añadir algunos vehículos a la autopista
for i in range(20):
    vehiculo = Vehiculo(i)
    autopista.agregar_vehiculo(vehiculo)

# Simular el tráfico en la autopista
for _ in range(10):
    # Cambiar el estado de los semáforos
    for semafaro in autopista.semafaro:
        semafaro.cambiar_estado()
    # Mostrar el estado actual de la autopista
    autopista.mostrar()
    # Mover los vehículos
    autopista.mover_vehiculos()
    # Revisar colisiones entre los vehículos
    autopista.revisar_colisiones()
    # Esperar un segundo antes de la siguiente iteración
    time.sleep(1)
