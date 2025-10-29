word = "abcdefd"
ch = "d"
new_word = ""

for letters in word:
	if letters in ch:
		new_word = word[3::-1] + word[3::1]
		print(new_word)
		