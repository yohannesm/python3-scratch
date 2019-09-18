#!usr/bin/python3

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n: 
        result.append(a)
        a, b = b, a + b
    return result

fVal = fib2(30000)
print(fVal)
