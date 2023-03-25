# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

gear = []

def gear_for_day(is_workday, is_sunny):
    if is_workday is True:
        gear.append("laptop")
        if is_sunny is False:
            gear.append("umbrella")
    else:
        gear.append("surfboard")
    return gear

is_workday = False
is_sunny = False
print(gear_for_day(is_workday, is_sunny))
