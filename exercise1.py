question = "What is your name? "
response = raw_input(question)
print(response[:1])
answer=""
if (response[:1].upper()=="B") : 
	answer = "Hello dummie, nice to meet you"
else:
	answer = "Hello, " +response +", nice to meet you"

print(answer)

#print("Hello, "+ raw_input("What is your name?") + ", nice to meet you")