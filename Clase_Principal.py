from seg_algoritmo0 import algoritmo0
from Seg_Algoritmos1 import algoritmo1
from Seg_Algoritmos2 import algoritmo2
from Seg_Algoritmo3 import algoritmo3
from Seg_Algoritmo4 import algoritmo4
from seg_algortimo5 import mergeSort
from Seg_algortimos6 import quicksort
from Seg_Algoritmo7 import heapsort
from Seg_Algoritmos8 import gnome_sort
from seg_algoritmo9 import bucketSort
from Seg_Algoritmo10 import bubbleSort
from Seg_Algortimo11 import stooge_sort
from seg_algoritmo12 import binary_insertion_sort
from seg_algoritmo13 import strand_sort
from seg_algoritmo14 import radixSort
from seg_algoritmo15 import burbuja_doble


import time
inicio = time.time()

#----------------------------capturas datos de txt ------------------------------------------------
# Abrir el archivo de texto en modo lectura
with open('Numeros.txt', 'r') as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()
    # Separar las líneas en elementos individuales y separar por comas
    lista_datos = [linea.strip() for linea in contenido.split(',')]

    lista_enteros = [int(x) for x in lista_datos]

print(lista_enteros)


#--------------------------imprime y pregunta----------------------------------------------------
if __name__== '__main__':
 fin_lista = int(input('¿Cuantos numeros quiere organizar?'))
 listaEstimacion = lista_enteros[0:fin_lista]

 print('lista que se va ordenar:',listaEstimacion)
 print('')
#------------------ALGORITMOS-------------------------------------------------------------------------------------------


#algoritmo 0- ORDENAMIENTO DE BUSBUJA----------------------------------------------------------------------------------
 inicio = time.perf_counter()
 #se llama la clase donde esta el metodo
 algoritmo_0= algoritmo0(listaEstimacion)
 listaOrdenada_0 = algoritmo_0.ordenamiento_de_burbuja(listaEstimacion)
 print('lista ordenada 0:',listaOrdenada_0)

#mide el tiempo
 fin = time.perf_counter()
 print((fin-inicio)*1000,'tiempo de ejecucion del ORDENAMIENTO DE BUSBUJA en milisegundos')


print('')

#algoritmo 1 - ordenamiento_por_insercion------------------------------------------------------------------------------
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
algoritmo_1 = algoritmo1(listaEstimacion)
listaOrdenada_1 = algoritmo_1.ordenamiento_por_insercion(listaEstimacion)
print('lista ordenada 1:',listaOrdenada_1)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de ordenamiento_por_insercion en milisegundos')





print('')

#algoritmo 2 - selectionSort------------------------------------------------------------------------------
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
algoritmo_2 = algoritmo2(listaEstimacion)
listaOrdenada_2 = algoritmo_2.selectionSort(listaEstimacion)
print('lista ordenada 2:',listaOrdenada_2)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de selectionSort en milisegundos')





print('')

#algoritmo 3 - shellSort------------------------------------------------------------------------------
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
algoritmo_3 = algoritmo3(listaEstimacion)
listaOrdenada_3 = algoritmo_3.shellSort(listaEstimacion)
print('lista ordenada 3:',listaOrdenada_3)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de shellSort en milisegundos')


print('')
#algoritmo 4- cocktailsort ----------------------------------------------------------------------------
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
algoritmo_4 = algoritmo4(listaEstimacion)
listaOrdenada_4 = algoritmo_4.cocktailSort(listaEstimacion)
print('lista ordenada 4:',listaOrdenada_4)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de cocktailSort en milisegundos')


print('')
#algoritmo 5-mergesort------------------------------------------------------------------------
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_5 = mergeSort(listaEstimacion)
print('lista ordenada 5:',listaOrdenada_5)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de mergesort en milisegundos')





#algoritmo 6 quicksort ----------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_6 = quicksort(listaEstimacion)
print('lista ordenada 6:',listaOrdenada_6)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de quicksort en milisegundos')




#algoritmo heapsort ----------------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_7 = heapsort(listaEstimacion)
print('lista ordenada 7:',listaOrdenada_7)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de heapsort en milisegundos')




#algoritmo 8 gnome_sort ------------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_8 = gnome_sort(listaEstimacion)
print('lista ordenada 8:',listaOrdenada_8)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de gnome_sort en milisegundos')




#algoritmo 9 bucketSort ---------------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_9 = bucketSort(listaEstimacion)
print('lista ordenada 9:',listaOrdenada_9)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de bucketSort en milisegundos')


#algoritmo 10 compAndSwap ---------------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_10 = bubbleSort(listaEstimacion)
print('lista ordenada 10:',listaOrdenada_10)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de compAndSwap en milisegundos')


#algoritmo 11  stooge_sort-----NO SIRVE-------------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_11 = stooge_sort(listaEstimacion)
print('lista ordenada 11:',listaOrdenada_11)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de stooge_sort en milisegundos')


#algoritmo 12 binary insertion sort -------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_12 = binary_insertion_sort(listaEstimacion)
print('lista ordenada 12:',listaOrdenada_12)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de binary insertion sort en milisegundos')


#algoritmo 13 strand_sort --------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_13 = strand_sort(listaEstimacion)
print('lista ordenada 13:',listaOrdenada_13)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de strand_sort sort en milisegundos')



#algoritmo 14 radixSort --------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_14 = radixSort(listaEstimacion)
print('lista ordenada 14:',listaOrdenada_14)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de radixSort sort en milisegundos')


#algoritmo 15 burbuja_doble--------------------------------------------------------------------------------
print('')
inicio = time.perf_counter()
# se llama la clase donde esta el metodo
listaOrdenada_15 = burbuja_doble(listaEstimacion)
print('lista ordenada 15:',listaOrdenada_15)
#mide el tiempo
fin = time.perf_counter()
print((fin - inicio) * 1000, 'tiempo de ejecucion de burbuja_doble sort en milisegundos')