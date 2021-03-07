def productSum(array):
    return productSumHelper(array, 1)

def productSumHelper(array, level):
    sum = 0
    for i in array:
        if type(i) == int:
            sum += i
        else:
            sum += productSumHelper(i, level + 1)
    return sum * level

productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])