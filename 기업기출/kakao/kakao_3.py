from collections import defaultdict
import math
def cal_time(s1, s2):
	add = 0
	s1_hour, s1_min = s1.split(':')
	s2_hour, s2_min = s2.split(':')
	s1_hour, s1_min, s2_hour, s2_min = int(s1_hour), int(s1_min), int(s2_hour), int(s2_min)
	temp = s2_min - s1_min
	if temp < 0:
		add += 60 + temp
		s2_hour -=1
	else:
		add += temp
	add += 60 * (s2_hour - s1_hour)
	return add



def solution(fees, records):
	answer = []
    
	info_dic = defaultdict(list)
	flag_dic = defaultdict(int)
	
	for rec in records:
		time, car_num, status = rec.split(' ')
		info_dic[car_num].append([time, status])
		flag_dic[car_num] += 1
	
	for car_num in flag_dic:
		if flag_dic[car_num] % 2 == 1:
			info_dic[car_num].append(['23:59', 'OUT'])
	
	info_dic = dict(sorted(info_dic.items()))

	for car_num in info_dic:
		stay_time = 0
		for i in range(0, len(info_dic[car_num]), 2):
			stay_time += cal_time(info_dic[car_num][i][0], info_dic[car_num][i + 1][0])
		charge = fees[1]
		over_time = stay_time - fees[0]
		if over_time > 0:
			charge += math.ceil(over_time / fees[2]) * fees[3]
		answer.append(charge)

			

	return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))