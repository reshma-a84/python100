# Passing Unlimited Arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5, 6, 7))