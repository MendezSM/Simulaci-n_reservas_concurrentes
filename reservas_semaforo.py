3import threading
from threading import Semaphore

asientos = 10
sem = Semaphore(3)

def reservar():
    global asientos

    with sem:
        if asientos > 0:
            asientos -= 1
            print("Reserva realizada. Asientos restantes:", asientos)
        else:
            print("No hay asientos disponibles")

for i in range(50):
    hilo = threading.Thread(target=reservar)
    hilo.start()

