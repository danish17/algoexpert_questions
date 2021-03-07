# O(n^2) time and O(n) space for storing triples
def threeNumberSum(array, targetSum):
    currentNumber = 0
    triples = []
    array = sorted(array)
    for currentNumber in range(len(array)):
        left = currentNumber + 1
        right = len(array) - 1
        while left < len(array) and left < right:
            pSum = array[currentNumber] + array[left] + array[right]
            if pSum == targetSum:
                triples.append([array[currentNumber], array[left], array[right]])
                left += 1
                right -= 1
            elif pSum < targetSum:
                left += 1
            elif pSum > targetSum:
                right -= 1
    return triples

threeNumberSum([-8, -6, 1, 2, 3, 5, 6, 12], 0)