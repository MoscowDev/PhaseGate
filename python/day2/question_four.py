from functools import reduce

my_list = [[1.5, 2.3, 3.7, 4.6], [5.1, 6.2, 7.3],[ 9.5, 10.1, 11.8,12.7]]


max = 0
def get_maximum(num,num2):
	if num > num2:
		return max == num
	else:
		return  num2

num = reduce(get_maximum,my_list)

print(num)





