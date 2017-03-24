import matriz
import threading
def main():
    
    lista = ['MENU\n''1.Determinante', '2.Transpuesta', '3.Inversa', '4.Escalar', '5.Matriz_Elevada', '6.Simetrica', '7.Identica',
             '8.Multiplicacion', '9.Suma', '10.Resta', '11.Salir']

    for i in lista:
        print i
    Z = int(input("Selecione La operacion que Desea Realizar "))

    def determinante():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.matriz_det(a)


    if Z == 1:
        hilo = threading.Thread(target=determinante, args=())
        hilo.start()
        hilo.join()

    def transpuesta():
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.transpuesta()

    if Z == 2:
        hilo1 = threading.Thread(target=transpuesta, args=())
        hilo1.start()
        hilo1.join()

    def matriz_inversa():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.matriz_inversa(a)

    if Z == 3:
        hilo2 = threading.Thread(target=matriz_inversa, args=())
        hilo2.start()
        hilo2.join()

    def matriz_numero():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.matriz_numero()

    if Z == 4:
        hilo4 = threading.Thread(target=matriz_numero, args=())
        hilo4.start()
        hilo4.join()

    if Z == 5:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_elevada()

    if Z == 6:
         matrizA = matriz.Matriz()
         matrizA.matrizSimetrica()

    def matrizidentica():
        matrizA = matriz.Matriz()
        matrizA.matrizidentica()
    if Z == 7:
        hilo3 = threading.Thread(target=matrizidentica, args=())
        hilo3.start()
        hilo3.join()


    if Z == 8:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.multiplicacionmatriz(filasA,columnasB,filasB,columnasA,a,b)

    if Z == 9:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if Z == 10:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.restamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if Z == 11:
        print "Vuelva Pronto Y Usa Esta Calculadora "
        M = True
    else:
        b = raw_input("Presione la tecla entrar para volver al menu")
        M = False



if __name__ == '__main__':
    main()