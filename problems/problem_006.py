# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.
age = 18
has_consent_form = ("No")
def can_skydive(age, has_consent_form):
    if age >= 18:
        print("This person can skydive")
        if has_consent_form == "No":
            print("but, you have to sign a consent form.")
        else:
            print("You are good to go!")
    else:
        print("This person cannot skydive")

can_skydive(age, has_consent_form)
