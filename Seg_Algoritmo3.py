# Metodo por ShellSort


class algoritmo3:
    def __init__(self, array):
        self.array = array
        self.selectionSor = self.shellSort(array)

    def shellSort(self,arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr
