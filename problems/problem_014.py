# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

##FIRST TRY BUT ORDER MATTERS SO DO AGAIN

#def can_make_pasta(ingredients):
#    if ingredients == ["flour", "eggs", "oil"]:
#        return True
#    else:
#        return False

#ingredients = ["flour", "oil", "eggs"]
#print (can_make_pasta(ingredients))

def can_make_pasta(ingredients):
    if (
        "flour" in ingredients and
        "eggs" in ingredients and
        "oil" in ingredients
        ):
        return True
    else:
        return False
ingredients = "eggs","flour","oil"
print(can_make_pasta(ingredients))
