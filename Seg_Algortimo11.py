def stooge_sort(arr):
    """
    Esta función implementa el algoritmo de ordenamiento Stooge Sort.
    """
    n = len(arr)
    if n <= 1:
        return arr
    if arr[0] > arr[n-1]:
        arr[0], arr[n-1] = arr[n-1], arr[0]
    if n > 2:
        t = int(n / 3)
        arr[:n-t] = stooge_sort(arr[:n-t])
        arr[t:n] = stooge_sort(arr[t:n])
        arr[:n-t] = stooge_sort(arr[:n-t])
    return arr
