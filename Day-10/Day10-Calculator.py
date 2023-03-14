def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+" : add,
    "-" : subtract,
    "*": multiply,
    "/": divide
    }

num1 = int(input("What's the first number? : "))
num2 = int(input("What's the second number? : "))

# for loop to print out symbols
for op in operations:
    print(op)

op_sym = input("Pick an operation from the line above : ")

cal_func = operations[op_sym]           #here cal_func is calling the op_sym, ie if the user enters +, then the value add will be picked from operations dictionary, thus cal_func = add
answer1 = cal_func(num1, num2)           # now answer will be = add(num1, num2) which will call the add function

print(f"{num1} {op_sym} {num2} = {answer1}")

op_sym = input("Pick another operation: ")
num3 = int(input("What's the next number? : "))
cal_func = operations[op_sym]
answer2 = cal_func(cal_func(num1,num2),num3)

print(f"{answer1} {op_sym} {num3} = {answer2}")
