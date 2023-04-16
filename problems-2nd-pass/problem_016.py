# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if x > 10 or x < 0:
        raise ValueError("Out of Bounds")
    if y > 10 or y < 0:
        raise ValueError("Out of Bounds")
    return x, y

print(is_inside_bounds(0,11))
