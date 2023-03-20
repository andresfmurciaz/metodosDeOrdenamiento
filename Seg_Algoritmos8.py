def gnome_sort(lista):
    n = len(lista)
    i = 0
    while i < n:
        if i == 0 or lista[i] >= lista[i - 1]:
            i += 1
        else:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
            i -= 1
    return lista
