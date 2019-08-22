#!/usr/bin/python3

def fizz_buzz(num):
    if (num % 5 == 0) and (num % 3 == 0):
        return "FizzBuzz"
    elif num % 5 == 0 :
        return "Buzz"
    elif num % 3 == 0 :
        return "Fizz"
    else:
        return str(num)

for i in range(1, 100):
    print( str(i) + "= " + fizz_buzz(i))

