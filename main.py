import random, timeit

# 01. Реализуйте алгоритм сортировки пузырьком на языке Python. Функция должна принимать список и возвращать
# отсортированный список
def bubbleSort(array):
	n = len(array)
	for i in range(n):
		swapped = False
		for j in range(0, n - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				swapped = True
		if not swapped:
			break
	return array

array = [random.randint(1, 100) for _ in range(10)]
print("Input : ", array)
print("Result: ", bubbleSort(array))

# 02. Реализуйте алгоритм сортировки выбором на языке Python. Функция должна принимать список и возвращать
# отсортированный список
def selectionSort(array):
	n = len(array)
	for i in range(n):
		min_idx = i
		for j in range(i + 1, n):
			if array[j] < array[min_idx]:
				min_idx = j
		array[i], array[min_idx] = array[min_idx], array[i]
	return array

array = [random.randint(1, 100) for _ in range(10)]
print("Input : ", array)
print("Result: ", selectionSort(array))

# 03. Сравнение алгоритмов: Сравните время выполнения двух алгоритмов сортировки (пузырьком, выбором) на
# одинаковых списках. Постройте график зависимости времени выполнения от размера списка для каждого алгоритма
size = 1000
array = [random.randint(1, size) for _ in range(size)]
print(array)

s = '''def bubbleSortTest():
	global array
	bubbleSort(array)
'''
print("bubbleSort: ", timeit.timeit(stmt=s))

s = '''def selectionSortTest():
	global array
	selectionSort(array)
'''
print("selectionSort: ", timeit.timeit(stmt=s))
