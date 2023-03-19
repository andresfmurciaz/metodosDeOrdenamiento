from seg_algoritmo0 import algoritmo0
from Seg_Algoritmos1 import algoritmo1


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

#------------------ALGORITMOS-------------------------------------------------------------------------------------------


#algoritmo 0- ORDENAMIENTO DE BUSBUJA----------------------------------------------------------------------------------
 inicio = time.perf_counter()
 #se llama la clase donde esta el metodo
 algoritmo_0= algoritmo0(listaEstimacion)
 listaOrdenada_0 = algoritmo_0.ordenamiento_de_burbuja(listaEstimacion)
 print('lista ordenada 0:',listaOrdenada_0)

#mide el tiempo
 fin = time.perf_counter()
 print((fin-inicio)*1000,'tiempo de ejecucion del algoritmo 0 en milisegundos')


"""""
#algoritmo 1 - ordenamiento_por_insercion------------------------------------------------------------------------------
inicio = time.time()
# se llama la clase donde esta el metodo
algoritmo_1 = algoritmo1(listaEstimacion)
listaOrdenada_1 = algoritmo_1.ordenamiento_por_insercion(listaEstimacion)
print('lista ordenada 0:',listaOrdenada_1)

#mide el tiempo
fin = time.time()
print((fin - inicio) * 1000, 'tiempo de ejecucion del algoritmo 1')

"""""





#algoritmo 2


#algoritmo 3


#algoritmo 4


#algoritmo 5


#algoritmo 6


#algoritmo 7


#algoritmo 8


#algoritmo 9



