# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


from itertools import combinations


def zero_sum_values(input_array):
    input_combinations = combinations(input_array, 3)
    input_combinations = list(input_combinations)
    result = []

    # print("iii", input_combinations)
    for each_combo in input_combinations:
        if (sum(each_combo) == 0):
            result.append(each_combo)

    return result


input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
# print(input_array)
print(zero_sum_values(input_array))
