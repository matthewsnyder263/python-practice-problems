# Write a function that meets these requirements.
#
# Name:       basic_calculator
# Parameters: left, the left number
#             op, the math operation to perform
#             right, the right number
# Returns:    the result of the math operation
#             between left and right
#
# The op parameter can be one of four values:
#   * "+" for addition
#   * "-" for subtraction
#   * "*" for multiplication
#   * "/" for division
#
# Examples:
#     * inputs:  10, "+", 12
#       result:  22
#     * inputs:  10, "-", 12
#       result:  -2
#     * inputs:  10, "*", 12
#       result:  120
#     * inputs:  10, "/", 12
#       result:  0.8333333333333334

def basic_calculator(num1, operation, num2):
    x = str(num1) + operation + str(num2)
    return int(x)

num1= 10
operation= "+"
num2= 12
print(basic_calculator(num1, operation, num2))