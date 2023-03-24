# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.
value1= 1
value2= 3
value3= 2

def max_of_three(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        return value1
    if value2 >= value1 and value2 >= value3:
        return value2
    else:
        return value3

print(max_of_three(value1, value2, value3))
