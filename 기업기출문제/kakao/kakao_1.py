from collections import defaultdict

def solution(id_list, report,k):
	answer = [0] * len(id_list)
	report = list(set(report))

	user = defaultdict(set)
	call = defaultdict(int)

	for string in report:
		a, b = string.split()
		user[a].add(b)
		call[b] += 1
	i = 0
	for id in id_list:
		for us in user[id]:
			if call[us] >= k:
				answer[i] += 1
		i += 1		
	return answer
