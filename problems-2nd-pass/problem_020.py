# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    attendees = len(attendees_list)
    members = len(members_list)
    if attendees >= members / 2:
        return True
    else:
        return False

attendees_list = ("matt","mark","luke","john")
members_list = ("rocky","shree","sarah","luke","john", "mike", "joe", "joseph")
print(has_quorum(attendees_list,members_list))
    # def has_quorum(attendees_list, members_list):
    # # num_attendees = the number of attendees
    # num_attendees = len(attendees_list)                 # solution
    # # num_members = the number of members
    # num_members = len(members_list)                     # solution
    # # If the num_attendees divided by the num_members is
    # # greater than 0.5
    # if num_attendees / num_members >= 0.5:              # solution
    #     # return True
    #     return True                                     # solution
    # # Otherwise
    # else:                                               # solution
    #     # return False
    #     return False                                    # solution
    # # pass                                              # problem
