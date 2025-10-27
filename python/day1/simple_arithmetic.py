import random



number = 0
answer = 0

for number in range(1,10):
	number_one = random.randint(11,100)
	number_two = random.randint(1,10)
	outcome = number_one - number_two
	number+1
print(f"what is {number_one} minus {number_two} : {outcome}")
	

store = number_one
number_one = number_two
number_two = store
 

print(f"what is {number_one} minus {number_two}")
answer = int(input( "enter first number: "))

if number_one - number_two == answer:
	print("you are right")

