multiple = 1
sum = 0

for number in range(1,11):
	if number % 4 == 0:
		for count in range(1,6):
			multiple = multiple * number
			sum += multiple 
		print(sum, end= " ")

	
		multiple = 1
		sum = 0



