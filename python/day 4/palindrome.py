def get_palindrome(my_list):
	storage = my_list
	count = 0
	for content in my_list:
		palindrome = ""
		for element in content :
			palindrome = element + palindrome

		if content  == palindrome:
			storage[count] = True;
		else:
			storage[count] = False;
		count+=1
	return storage
	
my_list  = ["madam", "kali", "hello", "noon"]
print(get_palindrome(my_list))