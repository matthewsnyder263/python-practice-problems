# Write a function that meets these requirements.
#
# Name:       username_from_email
# Parameters: a valid email address as a string
# Returns:    the username portion of the email address
#
# The username portion of an email is the substring
# of the email address that appears before the @
#
# Examples
#    * input:   "basia@yahoo.com"
#      returns: "basia"
#    * input:   "basia.farid@yahoo.com"
#      returns: "basia.farid"
#    * input:   "basia_farid+test@yahoo.com"
#      returns: "basia_farid+test"

# def username_from_email(string):
#     root_str = ""
#     at_index = string.find("@")
#     for i in range(at_index):
#         root_str += string[i]
#     return root_str

def username_from_email(string):
    at_index = string.find("@")
    root_str = string[at_index:]
    return root_str

print(username_from_email("msnyd87@gmail.com"))
