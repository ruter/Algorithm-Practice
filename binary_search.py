#-*- coding: UTF-8 -*-

def binSearch(arr, n, val):
    left = 0
    right = n - 1
    while(left <= right):
        middle = left + ((right - left) >> 1) # Faster than / 2
        if arr[middle] > val:
            right = middle - 1
        elif arr[middle] < val:
            left = middle + 1
        else:
            return middle
    return -1

# Test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 4

result = binSearch(arr, len(arr), val)

print result
