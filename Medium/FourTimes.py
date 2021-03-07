def arrayOfProducts(array):
    product = []
    for el in array:
        toAdd = 1
        for toMul in array:
            if el != toMul:
                toAdd *= toMul
        product.append(toAdd)
    return product

arrayOfProducts([5, 1, 4, 2])