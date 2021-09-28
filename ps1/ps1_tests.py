import math
import time
import random
import csv
from ps1 import merge, mergeSort, countSort, radixSort

max = 20

fastest = {
    'merge': [],
    'count': [],
    'radix': [],
}

total = 0

for U_p in range(1, max):
    U = 2**U_p
    for n_p in range(1, max):
        n = 2**n_p
        arr = [(random.randrange(0, U, 1), i) for i in range(n)]

        # timers
        start_time = time.time()
        mergeSort(arr)
        mergeTime = time.time() - start_time

        start_time = time.time()
        radixSort(arr, n, U, n)
        radixTime = time.time() - start_time

        start_time = time.time()
        countSort(arr, U)
        countTime = time.time() - start_time

        # fastest
        if min(mergeTime, countTime, radixTime) == mergeTime:
            fastest['merge'].append((n_p, U_p))
        elif radixTime < countTime:
            fastest['radix'].append((n_p, U_p))
        else:
            fastest['count'].append((n_p, U_p))

        total += 1

print(fastest)
print(total)
