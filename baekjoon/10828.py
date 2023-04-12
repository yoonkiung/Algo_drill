from inspect import isfunction
import sys
from unittest.mock import NonCallableMagicMock
sys.setrecursionlimit(10 ** 6)

class Stack:

	def __init__(self, capacity: int) -> None:
		self.table = [None] * capacity
		self.capacity = capacity
		self.ptr = 0

	def is_empty(self) -> bool:
		if self.ptr == 0:
			return True
		return False

	def is_full(self) -> bool:
		if self.ptr == self.capacity:
			return True
		return False

	def push(self, data: int) -> None:
		if self.is_full() == True:
			return
		self.table[self.ptr] = data
		self.ptr += 1
	
	def pop(self) -> None:
		if self.is_empty() == True:
			print(-1)
		else:
			print(self.table[self.ptr - 1])
			self.ptr -= 1

	def size(self) -> None:
		print(self.ptr)

	def empty(self) -> None:
		if self.is_empty() == True:
			print(1)
		else:
			print(0)

	def top(self) -> None:
		if self.is_empty() == True:
			print(-1)
		else:
			print(self.table[self.ptr - 1])

if __name__ == '__main__':
	n = int(input())
	stack = Stack(n)
	
	for i in range(n):
		input_list = list(input().split())
		if(input_list[0] == 'push'):
			stack.push(input_list[1])
		elif(input_list[0] == 'pop'):
			stack.pop()
		elif(input_list[0] == 'size'):
			stack.size()
		elif(input_list[0] == 'empty'):
			stack.empty()
		elif(input_list[0] == 'top'):
			stack.top()