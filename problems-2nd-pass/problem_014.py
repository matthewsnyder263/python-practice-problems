# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# def can_make_pasta(ingredients):
#     lst = ["flour", "eggs", "oil"]
#     lst2 =[]
#     for i in ingredients:
#         if i in lst:
#             lst2.append(i)
#     if lst == lst2:
#         return True
#     else:
#         return False
# print(can_make_pasta("flour, eggs", "oil"))

def can_make_pasta(ingredients):
    if ("flour" in ingredients and
        "eggs" in ingredients and
        "oil" in ingredients
        ):
        return True
    else:
        return False
print(can_make_pasta(["flour","eggs","butter"]))