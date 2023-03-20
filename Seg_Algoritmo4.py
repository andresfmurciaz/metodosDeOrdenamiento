#metodo burbuja bidireccional

class algoritmo4:
    def __init__(self, array):
        self.array = array
        self.cocktailSor = self.cocktailSort(array)
    def cocktailSort(self,arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped == True:
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if swapped == False:
                break
            swapped = False
            end = end - 1
            for i in range(end-1, start-1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            start = start + 1
        return arr
