# Write a class that meets these requirements.
#
# Name:       Person
#
# Required state:
#    * name, a string
#    * hated foods list, a list of names of food they don't like
#    * loved foods list, a list of names of food they really do like
#
# Behavior:
#    * taste(food name)  * returns None if the food name is not in their
#                                  hated or loved food lists
#                        * returns True if the food name is in their
#                                  loved food list
#                        * returns False if the food name is in their
#                                  hated food list
#
# Example:
#    person = Person("Malik",
#                    ["cottage cheese", "sauerkraut"],
#                    ["pizza", "schnitzel"])
#
#    print(person.taste("lasagna"))     # Prints None, not in either list
#    print(person.taste("sauerkraut"))  # Prints False, in the hated list
#    print(person.taste("pizza"))       # Prints True, in the loved list


# class Person
class Person:
    def __init__(self, name, hated_foods, loved_foods):
        self.name = name
        self.hated_foods = hated_foods
        self.loved_foods = loved_foods
    # method initializer with name, hated foods list, and loved foods list
        # self.name = name
        # self.hated_foods = hated_foods
        # self.loved_foods = loved_foods
    def taste(self, food):
        if food in self.hated_foods:
            return False
        elif food in self.loved_foods:
            return True
        else:
            return None


person = Person("Malik",
                ["cottage cheese", "sauerkraut"],
                ["pizza", "schnitzel"]
                )

print(person.taste("lasagna"))     # Prints None, not in either list
print(person.taste("sauerkraut"))  # Prints False, in the hated list
print(person.taste("pizza"))       # Prints True, in the loved list