save = 0.0  # variable to save previous answer


def add(num1, num2):
    return float(num1) + float(num2)


def sub(num1, num2):
    return float(num1)-float(num2)


def mul(num1, num2):
    return float(num1)*float(num2)


def div(num1, num2):
    return float(num1)/float(num2)


def pow(num1, num2):
    return float(num1)**float(num2)


gate = True
while gate:

    print("Welcome to the calculator!")

    first = (input("Enter your first number: "))  # takes in first input
    if first == "ans":
        first = save
    oper = input("Enter your op: ")
    second = (input("Enter your second number: "))  # takes in second input
    if second == "ans":
        second = save

    if oper == "*":
        answer = mul(first, second)  # multiplies the 2 inputs
        print(answer)
        save = answer

    if oper == "-":
        answer = sub(first, second)  # subtracts the 2 inputs
        print(answer)
        save = answer

    if oper == "+":
        answer = add(first, second)  # adds the 2 inputs
        print(answer)
        save = answer

    if oper == "**":
        # takes the first input raises it to the power of the second input
        answer = pow(first, second)
        print(answer)
        save = answer

    if oper == "/":
        answer = div(first, second)  # divides the 2 inputs
        print(answer)
        save = answer

    test = input("Continue y or n: ")  # user can continue to use calculator
    if test != "y":
        exit()
