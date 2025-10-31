my_list = []

def add_car(car):
    my_list.append(car)
    print(f"'{car}' A car added to the parking lot.")
    return my_list


def remove_car(*car):
    if car in my_list:
        my_list.remove(car)
        print(f"'{car}' removed from the parking lot.")
    else:
        print(f"'{car}' not found in the parking lot.")
    return my_list


def show_available_cars():
    if my_list:
        print("\nYour parking Lot:")
        for i, item in enumerate(my_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your parking lot is empty.")
