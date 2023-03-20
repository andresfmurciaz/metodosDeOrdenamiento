def heapsort(lista):
    n = len(lista)

    # construir un max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # extraer elementos de uno en uno
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # intercambiar
        heapify(lista, i, 0)

    return lista


def heapify(lista, n, i):
    # inicializar el mayor como la raíz
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    # ver si el hijo izquierdo del nodo es mayor que la raíz
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda

    # ver si el hijo derecho del nodo es mayor que la raíz
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha

    # cambiar la raíz si es necesario
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)
