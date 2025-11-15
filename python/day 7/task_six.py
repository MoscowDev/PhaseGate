multiple = 1
counter = 1
for number in range(1,11):
	if number % 4 == 0:
		for count in range(1,6):
			multiple = multiple * number
			print(multiple, end= " ")
		counter = 1
		multiple = 1



