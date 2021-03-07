'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here
def chooseX(nxt, prev, curr):
    i = 0
    while int(curr) - i >= int(nxt) and int(curr) - i > int(prev):
        i += 1
    return i


def checkIfStrictlyInc(array):
    array = [int(x) for x in array]
    idx = 0
    for idx in range(len(array) - 1):
        if array[idx] < array[idx + 1]:
            continue
        else:
            if idx == 0:
                x = chooseX(float("-inf"), array[idx + 1], array[idx])
                array[idx] = array[idx] - x
            else:
                x = chooseX(array[idx - 1], array[idx + 1], array[idx])
                array[idx] = array[idx] - x

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        arr = input()
        print(arr)
        checkIfStrictlyInc(arr.split(' '))
