from random import randint 

# machine_number = randint(1,10)
machine_number = 3
w = int (input("Guess the number:"))


if w < machine_number:
    print ("your guess is less than my number. Try again!")
elif w > machine_number:
    print ("your guess is greater than my number. Try again!")
else:
	print("Congratulations!")
