# 17. Write a program that serves as a basic calculator. It asks for two
# nbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to nbers. Deal with division by zero errors.


def operation(n1, n2, operator):
    if (operator == '+'):
        return n1 + n2
    elif (operator == '-'):
        return n1 - n2
    elif (operator == '*'):
        return n1 * n2
    elif (operator == '/'):
        try:
            return n1 / n2
        except ZeroDivisionError:
            return "Cannot divide by zero!"
    else:
        return "Please enter one of these operator(+, -, *, /)."


n1 = int(input("Enter the first number:"))
n2 = int(input("enter the second number:"))
operator = input("Enter the operator:")

print(operation(n1, n2, operator))
