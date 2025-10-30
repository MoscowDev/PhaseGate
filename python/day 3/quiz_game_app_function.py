def get_question_one():
	answer = input("Who is the president of Nigeria? ").lower()
	if answer == "tinubu":
		print(" Correct!")
		count = 1
	else:
		print(" Wrong! The correct answer is Tinubu.")
		count = 0
	return count
def get_question_two():
	answer = input("What is the capital of France? ").lower()
	if answer == "paris":
		print(" Correct!")
		count =1
	else:
		count = 0
		print(" Wrong! The correct answer is Paris.")
	return count 

def get_question_three():
	answer = input("Who owns the world? ").lower()
	if answer == "god":
		print(" Correct!")
		count =1
	else:
		count = 0
		print(" Wrong! The correct answer is God.")
	return count

def get_question_four():
	answer = input("Where is Tinubu from? ").lower()
	if answer == "nigeria":
		print(" Correct!")
		count =1
	else:
		count = 0
		print(" Wrong! The correct answer is Nigeria.")
	return count

def get_question_five(count):
	answer = input("What is the color of the sky? ").lower()
	if answer == "blue":
		print(" Correct!")
		count=1
	else:
		count = 0
		print(" Wrong! The correct answer is Blue.")

	return count
