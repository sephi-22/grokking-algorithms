# Factorial function (recursion)
def find_factorial(x):
    if x == 0:
        return 1
    return x * find_factorial(x - 1)


# Factorial function (loop)
def find_factorial_loop(x):
    fact = 1
    while x > 1:
        fact = fact * x
        x -= 1
    return fact


# Factorial function (loop2)
def find_factorial_loop2(x):
    if x == 0:
        return 1
    i = x - 1
    while i > 1:
        x = x * i
        i -= 1
    return x


# Factorial function (for loop):
def find_factorial_for_loop(x):
    if x == 0:
        return 1
    for i in range(1, x):
        x = x * i
    return x


print(find_factorial(5))
print(find_factorial_loop(5))
print(find_factorial_loop2(5))
print(find_factorial_for_loop(5))
