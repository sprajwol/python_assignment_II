# # 11. Create a variable, filename. Assuming that it has a three-letter
# # extension, and using slice operations, find the extension. For
# # README.txt, the extension should be txt. Write code using slice
# # operations that will give the name without the extension. Does your
# # code work on filenames of arbitrary length?

# filename = input("Enter the filename with extension:")
# name = filename[:-4]

# print(name)
# 11. Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?


filename = input("Enter a file name with three letter extension:")

only_filename = filename[:-4]
print(only_filename)
