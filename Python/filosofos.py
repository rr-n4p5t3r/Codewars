import threading
import time
# Desarrollado por Ricardo Rosero / https://github.com/rr-n4p5t3r
class Filosofo(threading.Thread):
    def __init__(self, nombre, tenedor_izquierdo, tenedor_derecho):
        """
        Inicializa un filosofo con su nombre y sus tenedores izquierdo y derecho.
        
        Parametros:
            nombre (str): El nombre del filosofo.
            tenedor_izquierdo (Fork): El tenedor izquierdo del filosofo.
            tenedor_derecho (Fork): El tenedor derecho del filosofo.
        """
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedor_izquierdo = tenedor_izquierdo
        self.tenedor_derecho = tenedor_derecho

    def run(self):
        """
        Bucle principal del filosofo: piensa, tiene hambre y come.
        """
        while True:
            print(f'{self.nombre} esta pensando.')
            time.sleep(2)  # Simula el tiempo que pasa pensando.
            print(f'{self.nombre} tiene hambre.')
            self.comer()  # Intenta comer.

    def comer(self):
        """
        Gestiona la accion de comer: adquiere los tenedores y simula la accion de comer.
        """
        tenedor_izquierdo, tenedor_derecho = self.tenedor_izquierdo, self.tenedor_derecho

        # Intentar adquirir los tenedores de manera ordenada para evitar interbloqueos.
        with tenedor_izquierdo:
            print(f'{self.nombre} ha tomado el tenedor izquierdo ({tenedor_izquierdo.nombre}).')
            with tenedor_derecho:
                print(f'{self.nombre} ha tomado el tenedor derecho ({tenedor_derecho.nombre}).')
                print(f'{self.nombre} esta comiendo.')
                time.sleep(2)  # Simula el tiempo que pasa comiendo.
                print(f'{self.nombre} ha terminado de comer y ha soltado ambos tenedores.')

class Tenedor:
    def __init__(self, nombre):
        """
        Inicializa un tenedor con un nombre y un cerrojo.
        
        Parametros:
            nombre (str): El nombre del tenedor.
        """
        self.nombre = nombre
        self.cerrojo = threading.Lock()

    def __enter__(self):
        """
        Adquiere el cerrojo del tenedor.
        """
        self.cerrojo.acquire()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Libera el cerrojo del tenedor.
        """
        self.cerrojo.release()

def main():
    """
    Funcion principal para inicializar tenedores y filosofos, y comenzar el ciclo de vida de los filosofos.
    """
    nombres_tenedores = ['Tenedor 1', 'Tenedor 2', 'Tenedor 3', 'Tenedor 4', 'Tenedor 5']
    tenedores = [Tenedor(nombre) for nombre in nombres_tenedores]  # Crear una lista de tenedores.

    nombres_filosofos = ['Filosofo 1', 'Filosofo 2', 'Filosofo 3', 'Filosofo 4', 'Filosofo 5']
    filosofos = [
        Filosofo(nombres_filosofos[i], tenedores[i], tenedores[(i + 1) % 5])
        for i in range(5)
    ]  # Crear una lista de filosofos con sus respectivos tenedores.

    for filosofo in filosofos:
        filosofo.start()  # Iniciar el hilo de cada filosofo.

    for filosofo in filosofos:
        filosofo.join()  # Esperar a que todos los hilos terminen (aunque esto nunca sucedera en este caso).

if __name__ == '__main__':
    main()
