# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        raise ValueError("Length needs to between 6 and 12 characters")
    lower = 0
    upper = 0
    digit = 0
    special = 0
    for i in password:
        if i.isupper():
            upper += 1

        elif i.islower():
            lower += 1

        elif i.isdigit():
            digit += 1

        elif i in ["$", "!", "@"]:
            special += 1

    if special == 0:
        raise ValueError("Need atleast 1 special character")
    if digit == 0:
        raise ValueError("Need atleast 1 number")
    if lower == 0:
        raise ValueError("Need atleast 1 lowerase")
    if upper == 0:
        raise ValueError("Need atleast 1 uppercase")
    return password, ("Your Password Is Valid")

password = ("asdfaS6f!")
print(check_password(password))
