# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


list_of_names = ['Sandy', 'Mandy', 'Dandy', 'Sam', 'John', 'James', 'Shane']


def searcher(name):
    for i in list_of_names:
        if (i == name):
            return True

    return False


s = searcher("John")
if (s == True):
    print("'John' is in the list.")
elif (s == False):
    print("not found")
