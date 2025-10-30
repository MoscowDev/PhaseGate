
from quiz_game_app_function import *
count = 0

while True:
	menu = """
	========== QUIZ GAME ===========
	1. Question 1
	2. Question 2
	3. Question 3
	4. Question 4
	5. Question 5
	6. See score
	7. Exit
"""

	print(menu)
    
	user = input("\n Enter the correct Answers (1-5): ")


	match user:

		case "1":
			score = get_question_one()
			count += score

		case "2": 
			score = get_question_two()
			count += score


		case "3":
			score = get_question_three()
			count += score


		case "4":
			score = get_question_four()
			count += score


		case "5":
			score = get_question_five(count)
			count += score


		case "7":
			print(" Exiting Quiz game. Goodbye!")
			
			break

		case "6":
			print(f" You only scored: {count}")

		case _:
			print(" Invalid choice! Please enter 1, 2, 3,4,5 or 6.")

