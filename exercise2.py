input = raw_input("What is the input string?")
while (not input) : 
	input = raw_input("Please enter a word: ")
print(input + " has "+ str(len(input)) + " characters" )