# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


def coverter(inputStr):
    result = inputStr[0].lower()
    for each_character in inputStr[1:]:
        if (each_character.isupper()):
            temp = "_" + each_character.lower()
            result = result + temp
        else:
            temp = each_character
            result = result + temp
    return result


inputStr = input("Enter the camel cased string: ")
print(coverter(inputStr))
