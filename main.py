import random

# 01. Напишите рекурсивную функцию для вычисления факториала числа n
def factorial(num):
	if num > 0:
		return num * factorial(num - 1)
	else:
		return 1

print("3!: ", factorial(3))
print("5!: ", factorial(5))

# 02. Напишите рекурсивную функцию для вычисления суммы всех элементов в списке.
# Убедитесь, что у функции есть базовый случай
def summ(array, key):
	if len(array) <= key:
		return 0
	else:
		return array[key] + summ(array, key + 1)

array = [random.randint(1, 10) for _ in range(5)]
print(array)
print("Summ: ", summ(array,  0))

# 03. Напишите рекурсивную функцию для выполнения бинарного поиска элемента в отсортированном списке.
# Функция должна возвращать индекс найденного элемента или -1, если элемент не найден
def binarySearchRecursive(array, low, high, target):
	if low <= high:
		mid = (low + high) // 2
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			return binarySearchRecursive(array, mid + 1, high, target)
		else:
			return binarySearchRecursive(array, low, mid - 1, target)
	else:
		return -1

array = [random.randint(1, 50) for _ in range(30)]
array.sort()
print(array)
target = random.randint(1, 50);
print(f"Targeted: '{target}' found on", binarySearchRecursive(array, 0, len(array), target), 'position')

#04. Напишите класс Stack, который реализует основные операции стека: push, pop, is_empty и peek
class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if not self.is_empty():
			return self.stack.pop()
		else:
			raise IndexError("Pop from an empty stack")

	def peek(self):
		if not self.is_empty():
			return self.stack[-1]
		else:
			raise IndexError("Peek from an empty stack")

	def is_empty(self):
		return len(self.stack) == 0

	def __str__(self):
		return ','.join(map(str, self.stack))

stackObject = Stack()
stackObject.push(8)
stackObject.push(55)
stackObject.push(18)
print(stackObject)
print(stackObject.pop())
print(stackObject.peek())
print(stackObject)

