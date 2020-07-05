# 19. Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


def brackets(inputString):
    stack = []
    brackets_dict = {"(": ")", "{": "}", "[": "]"}

    for each_bracket in inputString:
        if stack:
            topOfStack = stack[-1]
            if (each_bracket == brackets_dict[topOfStack]):
                stack.pop()
            else:
                stack.append(each_bracket)
        else:
            stack.append(each_bracket)

    if (len(stack) == 0):
        print(True)
    else:
        print(False)


inputString = r"([]}"
brackets(inputString)
