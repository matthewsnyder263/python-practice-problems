# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

# lst = [2, 5, 3]

# def calculate_average(values):
#     sum = 0
#     for num in values:
#         sum += num / len(values)
#     return sum


# print(calculate_average(values))

def calculate_average(values):
    if not values:
        return None
    else:
        return sum(values) / len(values)

lst = [5, 5, 100]
print(calculate_average(lst))
