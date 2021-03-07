# O(n^2) time // O(1) space
def selectionSort(array):
     i = 0
     j = 0
     for i in range(0, len(array)):
         for j in range(i, len(array)):
             if array[j] < array[i]:
                 array[i], array[j] = array[j], array[i]
     return array

