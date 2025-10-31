from mini_parking_system_function import *

while True:
	menu = """
	========== MINI PARKING SYSTEM ===========
	1. PARK CAR
	2. MOVE CAR
	3. SHOW PARKING STATUS
	4. Exit
	"""
	print(menu)
    
	user = int(input("\nEnter your choice (1-4): "))
		

	match user:
		case 1:        
			car = input(" Park your car: ")
			add_car(car)
          
		case 2:
			car = input("check out slot: ")
			remove_car(car)

		case 3:
			show_available_cars()
          

		case 4:
			print(" Exiting Mini parking System. Goodbye!")
			#break

		case _:
			print(" Invalid choice! Please enter 1, 2, 3, or 4.")
