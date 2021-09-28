#arr is array of (val, key) pairs
import math
import time
import random


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(arr, univsize):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def convertBase(num, b, U):
    remainders = []
    
    while num > 0:
        remainders.append(num % b)
        num = num // b

    converted = []
    for r in range(len(remainders)):
        converted.append(remainders[r])
    
    size = len(converted)
    maxSize = int(math.log(U, b)) + 1
    for i in range(maxSize - size):
        converted.append(0)

    return converted
    
def radixSort(arr, length, univsize, base):
    if length == 0 or length == 1:
        return arr

    for i in range(0, int(math.ceil(math.log(univsize, base)))):
        baseConvertedArr = []
        for (key, item) in arr:
            baseConvertedArr.append((convertBase(key, base, univsize), [key, item]))
        arr = baseConvertedArr
        radixArr = []
        others = []
        for (number, pair) in arr:
            radixArr.append((number[i], pair))
        radixSortedArr = countSort(radixArr, base)
        arr = []
        for (number, pair) in radixSortedArr:
            key, item = pair
            arr.append((key, item))
    return arr


# testing
arr = [(165, 'a'), (47, 'b'), (75, 'c'), (89, 'd'), (932, 'e'), (28, 'f'), (3, 'g'), (66, 'h')]
new = radixSort(arr, 8, 1000, 10)

for i in new:
    print(i)
 