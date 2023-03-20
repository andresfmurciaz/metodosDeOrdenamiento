def bucketSort(lista):
    # Obtener el valor máximo y la longitud de la lista
    max_value = max(lista)
    size = len(lista)

    # Crear una lista de buckets (contenedores) y llenarla con listas vacías
    bucket = [[] for _ in range(size)]

    # Asignar cada elemento de la lista en su correspondiente bucket
    for i in range(size):
        bucket_index = int(lista[i] * size / (max_value + 1))
        bucket[bucket_index].append(lista[i])

    # Ordenar los elementos dentro de cada bucket usando otro algoritmo de ordenamiento
    for i in range(size):
        bucket[i] = sorted(bucket[i])

    # Concatenar los elementos de los buckets en la lista de salida
    result = []
    for i in range(size):
        result += bucket[i]

    return result
