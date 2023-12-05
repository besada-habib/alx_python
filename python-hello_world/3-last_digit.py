#!/usr/bin/python3
from math import copysign
import random
number = random.randint(-10000, 10000)

last_digit_of_number = int(repr(number)[-1])
if last_digit_of_number > 5:
    print( "Last digit of",copysign(number, -1), "is", last_digit_of_number ,"is greater than 5")
elif last_digit_of_number == 0:
    print ("Last digit of",copysign(number,-1), "is", last_digit_of_number , "and is 0")
else:
    print("Last digit of",copysign(number,-1), "is", last_digit_of_number , "and is less than 6 and not 0")
    