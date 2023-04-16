# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    removed_lst = []
    values = values[0]
    values = values.replace("+",",")
    values_lst = values.split(",")
    for i in values_lst:
        i = int(i)
        removed_lst.append(i)

#    int_values_list = [int(i) for i in values_list]
#    print(int_values_list)
    return sum(removed_lst)

x = ["35+20+20+20+25+25+25+25+25+20+25+25+25+25+25+20"]
print(calculate_sum(x))
