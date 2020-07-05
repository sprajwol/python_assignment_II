# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

my_info = ('Prajwol', 'Shakya', 23)

friend_circle = []

friend_circle.append(my_info)

n = int(input("Enter a number for number of entries:"))

for i in range(n):
    input_fname = input("Enter first name of your friend:")
    input_lname = input("Enter last name of your friend:")
    input_age = int(input("Enter age of your friend:"))
    friend_info = (input_fname, input_lname, input_age)
    friend_circle.append(friend_info)

print(friend_circle)

sorted_friend_circle = sorted(friend_circle, key=lambda x: x[2])
print(sorted_friend_circle)
