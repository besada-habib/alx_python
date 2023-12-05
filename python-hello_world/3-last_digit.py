#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_of_number = int(repr(number)[-1])
if int(last_digit_of_number > 5):
    print( "Last digit of",number, "is", last_digit_of_number ,"is greater than 5")
elif int(last_digit_of_number == 0):
    print ("Last digit of",number, "is", last_digit_of_number , "and is 0")
else:
    print("Last digit of",number, "is", last_digit_of_number , "and is less than 6 and not 0")