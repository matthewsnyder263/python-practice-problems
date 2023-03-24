# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.


# ## MY ANSWER DOESN'T TAKE INTO ACCOUNT THE LENGHT
#def has_quorum(attendees_list, members_list):
#    if attendees_list >= (members_list / 2):
#        return True
#    else:
#        return False

# attendees_list = 49
# members_list = 100

# print(has_quorum(attendees_list, members_list))

def has_quorum(attendees_list, members_list):
    num_attendees = len(attendees_list)
    num_members = len(members_list)
    if num_attendees >= num_members / 2:
        return True
    else:
        return False

attendees_list = ["mike", 1, 2, 3, 4, 5]
members_list = ["jon", 1, 2,3,4,5,6,3,3,3,3,3]

print (len(members_list))
print (len(attendees_list))
print(has_quorum(attendees_list, members_list))

