multiple = 1
sum = 0
sum_two = 0
square = 0

for number in range(1,11):
	if number % 4 == 0:
		#multiple = 1
		sum = 0
		for count in range(1,6):
			multiple = multiple * number
			sum += multiple
		
		sum_two +=  sum
		square = sum_two*sum_two
print(square)

		




