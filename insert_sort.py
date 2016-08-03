#-*- coding: UTF-8 -*-
"""
1. 取 a[0]~a[i - 1] 为有序数列
2. 从 j = i - 1 开始向前寻找满足 a[j] > a[j + 1] 的数，并交换
3. 由1知 a[i] 前的数列已有序，且 a[j + 1] == a[i]，则当 a[j] <= a[j + 1]时，a[0]~a[j + 1]亦有序
"""

def insertSort(arr, n):
	for i in range(1, n):
		j = i - 1
		while j >= 0:
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
			j -= 1

# Test
arr = [3, 1, 2, 5, 4, 7, 9, 0, 8]
insertSort(arr, len(arr))

print arr