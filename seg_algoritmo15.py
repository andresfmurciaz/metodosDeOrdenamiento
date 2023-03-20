def burbuja_doble(lista):
    izquierda = 0
    derecha = len(lista) - 1
    cambio = True

    while izquierda < derecha and cambio:
        cambio = False

        # Burbuja hacia la derecha
        for i in range(izquierda, derecha):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                cambio = True

        derecha -= 1

        # Burbuja hacia la izquierda
        for i in range(derecha, izquierda, -1):
            if lista[i] < lista[i-1]:
                lista[i], lista[i-1] = lista[i-1], lista[i]
                cambio = True

        izquierda += 1

    return lista
