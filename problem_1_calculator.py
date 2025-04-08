from testhelper import test

def calculate(input1, operator, input2):

    if operator == "+":
        result = input1 + input2
    elif operator == "-":
        result = input1 - input2
    elif operator == "*":
        result = input1 * input2
    elif operator == "/":
        result = input1 / input2
    else:
        result = "Invalid operator"
    return result

input1 = int(input('Enter a number: '))
operator = input('Enter a form of operations: ')
input2 = int(input('Enter a number: '))

result = calculate(input1, operator, input2)
print(f"The result is: {result}")