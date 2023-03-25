# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    if len(values) == 0:
        return None
    total = 0 
    for val in values:
        total = total + val
    return total
    
lst = [2,3,4,5]
print (calculate_sum(lst))
