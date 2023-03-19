

#----------------------------capturas datos de txt ------------------------------------------------
# Abrir el archivo de texto en modo lectura
with open('Numeros.txt', 'r') as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()
    # Separar las líneas en elementos individuales y separar por comas
    lista_datos = [linea.strip().split(',') for linea in contenido.split('\n')]

print(lista_datos)

