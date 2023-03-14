from art import logo
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


def calculator():
    print(logo)
    num1 = float(input("What's the first number? : "))


    # for loop to print out symbols
    for op in operations:
        print(op)
    should_continue = True

    while should_continue:


        op_sym = input("Pick an operation from the line above : ")
        num2 = float(input("What's the second number? : "))

        cal_func = operations[op_sym]           #here cal_func is calling the op_sym, ie if the user enters +, then the value add will be picked from operations dictionary, thus cal_func = add
        answer = cal_func(num1, num2)           # now answer will be = add(num1, num2) which will call the add function

        print(f"{num1} {op_sym} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation :") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
    

calculator()


