def get_palindrome(my_list):
	
	count = 0
	for content in my_list:
		palindrome = ""
		for element in content :
			palindrome = element + palindrome

		if content  == palindrome:
			 my_list[count] = True;
		else:
			 my_list[count] = False;
		count+=1
	return my_list
	
my_list  = ["madam", "kali", "hello", "noon"]
print(get_palindrome(my_list))