

#----------------------------capturas datos de txt ------------------------------------------------
# Abrir el archivo de texto en modo lectura
with open('Numeros.txt', 'r') as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()
    # Separar las líneas en elementos individuales y separar por comas
    lista_datos = [linea.strip() for linea in contenido.split(',')]
print(lista_datos)

#--------------------------imprime y pregunta
if __name__== '__main__':
 fin_lista = int(input('¿Cuantos numeros quiere organizar?'))
listaEstimacion = lista_datos[0:fin_lista]
print(listaEstimacion)



