
from quiz_game_app_function import *

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
			
			get_question_one()
            

		case "2": 
			get_question_two()
            

		case "3":
			get_question_three()
            


		case "4":
			get_question_four()


		case "5":
			get_question_five()


		case "7":
			print(" Exiting Quiz game. Goodbye!")
			
			break

		case "6":
			get_count()

		case _:
			print(" Invalid choice! Please enter 1, 2, 3,4,5 or 6.")

