from seg_algoritmo0 import algoritmo0
from Seg_Algoritmos1 import algoritmo1
from Seg_Algoritmos2 import algoritmo2
from Seg_Algoritmo3 import algoritmo3
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

"""""
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




#algoritmo 2
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



#algoritmo 3

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

"""""

#algoritmo 4


#algoritmo 5


#algoritmo 6


#algoritmo 7


#algoritmo 8


#algoritmo 9



