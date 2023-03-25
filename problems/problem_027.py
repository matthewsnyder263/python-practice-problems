# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    greatest_value = max(values)
    for i in values:
        return greatest_value 

lst = [52,32,9,28]
print(max_in_list(lst))
