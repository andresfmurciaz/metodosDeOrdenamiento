import random
import time
inicio = time.time()

#metodo burbuja 
class algoritmo0:
    def __init__(self,lista):
        self.lista=lista
        self.burbuja =self.ordenamiento_de_burbuja(lista)

    def ordenamiento_de_burbuja(self,lista):
        n = len(lista)

        for i in range(n):
         for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

"""
if __name__== '__main__':
 tamano_de_lista = int(input('De que tamano sera la lista?'))

 lista2 = [random.randint(0,1000 ) for i in range(tamano_de_lista)]
 print(lista2)
 hola1= algoritmo0(lista2)
 listaordenada = hola1.ordenamiento_de_burbuja(lista2)
 print(listaordenada)
fin = time.time()
print(fin-inicio),input('tiempo de ejecucion del algoritmo')
"""
