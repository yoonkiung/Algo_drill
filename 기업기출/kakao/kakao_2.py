from math import ceil, sqrt


def conv(n, k):
	answer = ''
	arr = []
	for i in range(k):
		arr.append(i)
	while n > 0:
		answer = answer + str(arr[n % k])
		n = n // k
	return answer[::-1]

def is_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	for i in range(2, ceil(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def solution(n, k):
	answer = 0
	conv_str = conv(n, k)
	arr = conv_str.split('0')
	print(arr)
	for num in arr:
		if num == '':
			continue
		conv_num = int(num)
		if is_prime(conv_num) == True:
			print(conv_num)
			answer += 1
	return answer