# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    if attendees_list >= (members_list / 2):
        return True
    else:
        return False

attendees_list = 49
members_list = 100

print(has_quorum(attendees_list, members_list))


#set variable for total in attendence
#    if total_attendees =
#set variable to 50% of members_list
#see if var1 >= var2
#return true else false
