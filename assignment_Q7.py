# 7. Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.
import statistics
list_of_data = [("Prajwol", "Shakya", 23), ("Momika", "Sherestha", 22), ("Ashish", "Maharjan", 24), ("Shirisha", "Maharjan", 22), ("Ananda", "Pandey", 25),
                ("Pramisha", "Kapali", 18), ("Adarsha", "Thapa", 20), ("Tejwol", "Shakya", 18), ("Aayushma", "Shakya", None), ("Shoojan", "Maharjan", 28), ("Subha", "Maharjan", 22)]

age_list = [each_tuple[2]
            for each_tuple in list_of_data if each_tuple[2] != None]
print(age_list)
avg_age = statistics.mean(age_list)

for each_tuple in list_of_data:

    if (each_tuple[2] == None):
        print(each_tuple[0], "!!!No Data!!!")
    elif (each_tuple[2] < avg_age):
        print(each_tuple[0], "young")
    elif (each_tuple[2] > avg_age):
        print(each_tuple[0], "old")
