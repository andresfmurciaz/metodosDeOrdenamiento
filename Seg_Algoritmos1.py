import random
import time
inicio = time.time()
#metodo inserción
class algoritmo1:
    def __init__(self,lista):
        self.lista=lista
        self.ordenamiento_x_insercion =self.ordenamiento_por_insercion(lista)

    def ordenamiento_por_insercion(self,lista):
            for i in range(1, len(lista)):
                actual = lista[i]
                j = i - 1
                while j >= 0 and actual < lista[j]:
                    lista[j + 1] = lista[j]
                    j -= 1
                lista[j + 1] = actual

            return lista



