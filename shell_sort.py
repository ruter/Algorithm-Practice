#-*- coding: UTF-8 -*-

"""
1. 取增量gap初始值为数组大小 n/2
2. 从数组第gap个元素开始，每个元素与自己组内的数据进行直接插入排序
3. 改变gap值为 gap/2，直到 gap <= 0
"""
def shellSort(arr, n):
	gap = n / 2
	while gap > 0:
		for i in range(gap, n):
			j = i - gap
			while j >= 0 and arr[j] > arr[j + gap]:
				arr[j], arr[j + gap] = arr[j + gap], arr[j]
				j -= gap
		gap /= 2
		
# Test
arr = [3, 1, 2, 5, 4, 7, 9, 0, 8]
shellSort(arr, len(arr))

print arr
