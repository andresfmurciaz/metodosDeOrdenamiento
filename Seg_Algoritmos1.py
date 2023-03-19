import random
import time
inicio = time.time()
#metodo inserción
class algoritmo1:
    def __init__(self,lista):
        self.lista=lista
        self.ordenamiento_x_insercion =self.ordenamiento_por_insercion(lista)

    def ordenamiento_por_insercion(lista):

        for indice in range(1, len(lista)):
            valor_actual = lista[indice]
            posicion_actual = indice

            while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
                lista[posicion_actual] = lista[posicion_actual - 1]
                posicion_actual -= 1

            lista[posicion_actual] = valor_actual

            return lista



