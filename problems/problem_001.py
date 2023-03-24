# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.
value1 = 3
value2 = 5
def minimum_value(value1, value2):
    if value1 < value2:
        print (value1)
    elif value2 < value1:
        print (value2)
    elif value1 == value2:
        print ("either")

minimum_value(value1, value2)
