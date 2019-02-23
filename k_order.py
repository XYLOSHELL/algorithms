from random import *

def k_order_stat(array, k):
    if len(array) == 1:
        return array[0]
    x = array[randint(0, len(array) - 1)]
    left = [y for y in array if y < x]
    right = [y for y in array if y >= x]
    if len(left) >= k:
        return k_order_stat(left, k)
    elif len(left) == 0:
        return array[0]
    else:
        return k_order_stat(right, k - len(left))

k = int(input())
array = [int(s) for s in input().split()]
print(k_order_stat(array, k))