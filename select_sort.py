#-*- coding: UTF-8 -*-

"""
1. 初始数组无序，选取首元素a[i]，i = 0
2. 从i~n-1选取最小元素，与a[i]交换
3. i++，重复第2步
"""
def selectSort(arr):
	for i in range(0, len(arr)):
		minIndex = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[minIndex]:
				minIndex = j
		arr[i], arr[minIndex] = arr[minIndex], arr[i]

# Test
arr = [75, 6, 57, 88, 60, 42, 83, 73, 48, 85]
selectSort(arr)
 
print arr
