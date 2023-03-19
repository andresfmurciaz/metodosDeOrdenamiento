import sys
import time
inicio = time.time()
# Metodo por seleccion
array = [20, 5, 21, 6, 23, 7, 34, 999, 68]


def selectionSort(array):
    for i in range(len(array)):

        idxDes = i
        for j in range(i+1, len(array)):
            if array[idxDes] > array[j]:
              idxDes = j

        array[i], array[idxDes] = array[idxDes], array[i]


selectionSort(array)
print("Array Ordenado:")
for i in range(len(array)):
    print("%d" % array[i])
    
fin = time.time()
print(fin-inicio),input('tiempo de ejecucion del algoritmo')