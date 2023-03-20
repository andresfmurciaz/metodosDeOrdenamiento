def strand_sort(lst):
    if len(lst) == 0:
        return []

    # Dividir la lista en subsecuencias ordenadas
    subseqs = [[lst[0]]]
    for i in range(1, len(lst)):
        if lst[i] > subseqs[-1][-1]:
            subseqs[-1].append(lst[i])
        else:
            subseqs.append([lst[i]])

    # Fusionar subsecuencias hasta que la lista esté ordenada
    while len(subseqs) > 1:
        res = []
        i = 0
        while i < len(subseqs) - 1:
            merged = merge(subseqs[i], subseqs[i+1])
            res.append(merged)
            i += 2
        if i == len(subseqs) - 1:
            res.append(subseqs[-1])
        subseqs = res

    return subseqs[0]

def merge(lst1, lst2):
    res = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    if i == len(lst1):
        res += lst2[j:]
    else:
        res += lst1[i:]
    return res
