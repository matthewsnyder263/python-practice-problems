# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(input):
    list1 = []
    list2 = []
    first_half = len(input) // 2 + (len(input) % 2)
    for i in range(first_half):
        list1.append(input[i])
    for i in range(first_half, len(input)):
        list2.append(input[i])
    print(list1)
    print(list2)
    
input = [1,2,3,4]
halve_the_list(input)