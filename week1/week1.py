# Functions
def circle_shaded_area(radius_outside, radius_inside):
    area_outside = 3.14 * radius_outside ** 2
    area_inside = 3.14 * radius_inside ** 2
    area_shaded = area_outside - area_inside
    return area_shaded

# Using logical operators to test functions
answer_is_incorrect = (area_shaded > area_outside) || (area_shaded < area_inside)

# Program for student's fundraising event?
