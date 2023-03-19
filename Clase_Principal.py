from seg_algoritmo0 import algoritmo0
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

#------------------ALGORITMOS---------------------------------------

#algoritmo 0- ORDENAMIENTO DE BUSBUJA
 algoritmo_0= algoritmo0(listaEstimacion)
 listaOrdenada_0 = algoritmo_0.ordenamiento_de_burbuja(listaEstimacion)
 print(listaOrdenada_0)
#mide el tiempo
 fin = time.time()
 print(fin-inicio),input('tiempo de ejecucion del algoritmo')


#algoritmo 1


#algoritmo 2


#algoritmo 3


#algoritmo 4


#algoritmo 5


#algoritmo 6


#algoritmo 7


#algoritmo 8


#algoritmo 9



