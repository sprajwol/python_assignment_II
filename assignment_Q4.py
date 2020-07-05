# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

friends_name_list = []
print("Original id of list", id(friends_name_list))
n = int(input("Enter a number for number of entries:"))

for i in range(n):
    input_name = input("Enter name of your friend:")
    friends_name_list.append(input_name)

print("id of list after appending data", id(friends_name_list))

# The id of the list doesn't change
friends_name_list = sorted(friends_name_list)

print("First item in the list:{}".format(friends_name_list[0]))
print("Second item in the list:{}".format(friends_name_list[1]))

# If the inputs i gave were [Annie, Shirisha, Ashish], The first item would be 'Annie' and second would be 'Ashish'.
