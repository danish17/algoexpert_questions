# O(n) reduced from 3n time | O(n) space
def arrayOfProducts(array):
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]
    products = [1 for _ in range(len(array))]
    left, right = 1, 1
    for idx in range(len(array)):
        leftProducts[idx] = left
        left *= array[idx]
    for idx in reversed(range(len(array))):
        rightProducts[idx] = right
        right *= array[idx]
    for idx in range(len(array)):
        products[idx] = leftProducts[idx] * rightProducts[idx]

    return products

arrayOfProducts([5, 1, 4, 2])