# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.


def binary_search(sorted_seq, query):
    low_val = 0
    mid_val = 0
    high_val = len(sorted_seq) - 1

    while (low_val <= high_val):
        mid_val = (low_val + high_val) // 2

        if (sorted_seq[mid_val] < query):
            low_val = mid_val + 1
        elif (sorted_seq[mid_val] > query):
            high_val = mid_val - 1
        else:
            return mid_val

    return -1


sorted_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(sorted_seq)
n = int(input("Enter the number you want to find:"))
result = binary_search(sorted_seq, n)

if (result == -1):
    print("The number is not in the sequence.")
else:
    print(f"The number is in the index {result}")
