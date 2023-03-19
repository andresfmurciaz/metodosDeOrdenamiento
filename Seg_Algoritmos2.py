import sys

class algoritmo2:

    def __init__(self, array):
        self.array = array
        self.selectionSor = self.selectionSort(array)


    def selectionSort(self,lista):
        """
        Ordena una lista de enteros utilizando el algoritmo Selection Sort y retorna la lista ordenada.
        """
        n = len(lista)
        for i in range(n):
            # Busca el mínimo elemento en el resto de la lista
            min_idx = i
            for j in range(i + 1, n):
                if lista[j] < lista[min_idx]:
                    min_idx = j
            # Intercambia el mínimo elemento con el primer elemento sin ordenar
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
        return lista





