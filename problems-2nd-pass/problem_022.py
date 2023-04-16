# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    lst=[]
    if is_workday and is_sunny:
        lst.append("laptop")
    elif is_workday and not is_sunny:
        lst.append("umbrella")
    else:
        lst.append("surfboard")
    return lst 

print(gear_for_day(True, True))
