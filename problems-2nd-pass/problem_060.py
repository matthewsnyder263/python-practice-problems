# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]

def only_odds(numbers):
    new_lst = []
    for i in numbers:
        if i % 2 != 0:
            new_lst.append(i)
    return new_lst
       
numbers = [ 2, 4]
print(only_odds(numbers))
