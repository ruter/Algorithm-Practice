#-*- coding: UTF-8 -*-

"""
1. Pick up the first element as a reference number, saved to variable x
2. From the back forward to find an element smaller than x
3. Saved to list where index is l, then l + 1
4. Start at index l to find an element bigger than or equal to x
5. Saved to list where index is r, then r - 1
6. Repeat 2 to 5, until l >= r
7. Put x to list where index is l
8. Last, recursive call the function
"""
def partition(arr, l, r):
	x = arr[l]
	while l < r:
		while l < r and arr[r] >= x:
			r -= 1
		if l < r:
			arr[l] = arr[r]
			l += 1
 
		while l < r and arr[l] < x:
			l += 1
		if l < r:
			arr[r] = arr[l]
			r -= 1
 
	arr[l] = x
	return l
 
def quickSort(arr, l, r):
	if l < r:
		i = partition(arr, l, r)
		quickSort(arr, l, i - 1)
		quickSort(arr, i + 1, r)
 
arr = [75, 6, 57, 88, 60, 42, 83, 73, 48, 85]
quickSort(arr, 0, len(arr) - 1)
 
print arr

# Merge into one function
# def quickSort(arr, left, right):
# 	if left < right:
# 		i = left
#		j = right
#		x = arr[left]
# 		while i < j:
# 			while i < j and arr[j] >= x:
# 				j -= 1
# 			if i < j:
# 				arr[i] = arr[j]
# 				i += 1
			
# 			while i < j and arr[i] < x:
# 				i += 1
# 			if i < j:
# 				arr[j] = arr[i]
# 				j -= 1
			
# 		arr[i] = x
# 		quickSort(arr, left, i - 1)
# 		quickSort(arr, i + 1, right)

# # Test
# arr = [75, 6, 57, 88, 60, 42, 83, 73, 48, 85]
# quickSort(arr, 0, len(arr) - 1)

# print arr