#Hank Warner, p1, 10-2-19


import random

RollNum = input("Total Rolls :")
Roll = random.randint(1, 6)

x = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

while x < int(RollNum):
	print(Roll)
	x += 1
	
	if Roll == 1:
		ones += 1
	if Roll == 2:
		twos += 1
	if Roll == 3:
		threes += 1
	if Roll == 4:
		fours += 1
	if Roll == 5:
		fives += 1
	if Roll == 6:
		sixes += 1
print("1s: " + int(ones))
print("2s: " + int(twos))
print("3s: " + int(threes))
print("4s: " + int(fours))
print("5s: " + int(fives))
print("6s: " + int(sixes))

