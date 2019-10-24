import random

mysteryNum = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Pick a # between 1 and 100."))
	score = score + 1
	x = 1
	if guess == mysteryNum:
		print("Good guess")
		break
	elif guess > mysteryNum:
		print("Too high, try again")
	else:
		print("No, too low")
	if score > 15:
		print("you got to over 15 guesses. Get better")
		x = x + 1
		while x > 20:
			print("Get Better")
			break

print("It took you " + str(score) +" guesses")
