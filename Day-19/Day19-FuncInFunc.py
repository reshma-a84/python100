def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calculator(n1, n2, func): # Function calculator is a higher order function - a function that can work with other function
    return func(n1, n2)


result = calculator(2, 3, add)   # Here we are calling a function inside another function
print(result)
