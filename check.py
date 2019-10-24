#This is a check & review to be sure nothing wasa lost over break

#Hank Warner
#P1

#Variable declaration and assignment

string = "This should be a string"
number = 0

#while loops

while number < 10:
	number += 1
	print(number)

#Print name 100 times

x = 0
Name = "Hank"
while x < 100:
	x += 1
	print(Name)

#String Concantanation

name = "Hank"
print("Hello " + name)

#Make a variable with favorite movie and print "My favorite move is : "

movie = "Saving Private Ryan"
print("My favorite movie is : " + movie)

#input

myName = input("What is your name ? ")
print("Your name is : " + myName)

#Prompt for favorite song, pring your favorite song is:

song = input("What is your favorite song ? ")
print( myName + "'s favorite song is : " + song)

#Casting, or changing the type of the variable

myNumber = 43
print("My Number is : " + str(myNumber))

num1 = input("Enter a number : ")
num1 = int(num1) + 10
print("Num1 + 10 is " + str(num1))

#ask for 2 numbers, add then print

1stnumber = int(input("Enter a number"))
2ndnumber = int(input("Enter another number"))

3rdnumber = int(1stnumber) + int(2ndnumber)

print("Your numbers added together are : " str(3rdnumber))

 #if & else

 1num = int(input("type a number"))
 if 1num > 100:
 	print("Your number is bigger than 100")
 elif 1num == 100:
 	print("Your nmuber = 100")
 else:
 	print("Your number is less than or equal to 100")

 #ask if day is birthday, if so print happy birthday

 day = input("is today your birthday? ")
 if day = str("yes"):
 	print("Happy birthday ")