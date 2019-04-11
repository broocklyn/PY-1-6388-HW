
__author__ = 'Учускин Павел Валерьевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	fib_p_p = 1
	fib_p = 1
	fib = 0
	if n == 1:
		print(fib_p_p, fib_p, end = ' ')
	elif n == 2:
		print(fib_p, end = ' ')
	for i in range(3,m + 1):
		fib = fib_p_p + fib_p
		fib_p_p = fib_p
		fib_p = fib
		if i >= n and i <= m:
			print(fib, end = ' ')
		elif i > m:
			return
fibonacci(3,10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
	sort_to_max_list = []
	for i in range(len(origin_list)):
		min = float('inf')
		for j in origin_list:
			if j <= min:
				min = j
		sort_to_max_list.append(min)
		origin_list.remove(min)
	print(sort_to_max_list)
	
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter(func,x):
	a = []
	b = iter(x)
	if func == None:
		for i in b:
			if i != 0:
				if i != '':
					a.append(i)
		return iter(a)
	else:
		for i in b:
			if func(i) == True:
				a.append(i)
	return iter(a)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

