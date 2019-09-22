# program to find smallest missing positive number from array
import numpy as np

array = [1, 6,7]

if len(array) == 1:
    if array[0] == 1:
        print(2)
    else:
        print(1)
else:
    if max(array) < 1:
        print(1)
    else:
        smallest = list(np.zeros(max(array)))
        for i in range(max(array)):
            if i + 1 in array:
                smallest[i] = 1
        if 0 in smallest:
            print(smallest.index(0) + 1)
        else:
            print(max(array) + 1)
