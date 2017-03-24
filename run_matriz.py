import matriz
import threading


matrizA = matriz.Matriz()
matrizB = matriz.Matriz()
def crearMatrizA():

    matrizA.crearMatrizA()
    matrizA.llenarmatrizA()
    matrizA.imprime_matriz()


def crearMatrizB():
    print "matriz B"

    matrizB.crearMatrizB()
    matrizB.llenarmatrizB()
    matrizB.imprime_matriz()

hilo = threading.Thread(target= crearMatrizA(), args=())
hilo.start()
hilo = threading.Thread(target= crearMatrizB(), args=())
hilo.start()
