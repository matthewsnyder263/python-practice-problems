# Write a function that meets these requirements.
#
# Name:       sum_two_numbers
# Parameters: two numerical parameters
# Returns:    the sum of the two numbers
#
# Examples:
#    * x: 3
#      y: 4
#      result: 7

def sum_two_numbers(x, y):
    return sum([x, y])

x = 3
y = 4
print(sum_two_numbers(x, y))
