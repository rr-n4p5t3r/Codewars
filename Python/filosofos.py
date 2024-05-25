import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        """
        Inicializa un filosofo con su nombre y sus tenedores izquierdo y derecho.
        """
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        """
        Bucle principal del filosofo: piensa, tiene hambre y come.
        """
        while True:
            print(f'{self.name} esta pensando.')
            time.sleep(2)  # Simula el tiempo que pasa pensando.
            print(f'{self.name} tiene hambre.')
            self.dine()  # Intenta comer.

    def dine(self):
        """
        Gestion de la accion de comer: adquiere los tenedores y simula la accion de comer.
        """
        fork1, fork2 = self.left_fork, self.right_fork

        # Intentar adquirir los tenedores de manera ordenada para evitar interbloqueos.
        with fork1:
            print(f'{self.name} ha tomado el tenedor izquierdo ({fork1.name}).')
            with fork2:
                print(f'{self.name} ha tomado el tenedor derecho ({fork2.name}).')
                print(f'{self.name} esta comiendo.')
                time.sleep(2)  # Simula el tiempo que pasa comiendo.
                print(f'{self.name} ha terminado de comer y ha soltado ambos tenedores.')

class Fork:
    def __init__(self, name):
        """
        Inicializa un tenedor con un nombre y un bloqueo.
        """
        self.name = name
        self.lock = threading.Lock()

    def __enter__(self):
        """
        Adquiere el bloqueo del tenedor.
        """
        self.lock.acquire()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Libera el bloqueo del tenedor.
        """
        self.lock.release()

def main():
    """
    Funcion principal para inicializar tenedores y filosofos, y comenzar el ciclo de vida de los filosofos.
    """
    fork_names = ['Tenedor 1', 'Tenedor 2', 'Tenedor 3', 'Tenedor 4', 'Tenedor 5']
    forks = [Fork(name) for name in fork_names]  # Crear una lista de tenedores.

    philosopher_names = ['Filosofo 1', 'Filosofo 2', 'Filosofo 3', 'Filosofo 4', 'Filosofo 5']
    philosophers = [
        Philosopher(philosopher_names[i], forks[i], forks[(i + 1) % 5])
        for i in range(5)
    ]  # Crear una lista de filosofos con sus respectivos tenedores.

    for philosopher in philosophers:
        philosopher.start()  # Iniciar el hilo de cada filosofo.

    for philosopher in philosophers:
        philosopher.join()  # Esperar a que todos los hilos terminen (aunque esto nunca sucedera en este caso).

if __name__ == '__main__':
    main()
