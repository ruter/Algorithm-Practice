# -*- coding: utf-8 -*-

# 递归
def fib1(n):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)

# 迭代
def fib2(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a

n = raw_input()
print "recursive:"
for i in range(n):
	print(fib1(i))

print "iteration:"
for i in range(n):
	print(fib2(i))