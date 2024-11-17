# set_1 = {1,2,3}
# set_2 = {3,4,5}
# union_set = set_1 & set_2
# print(union_set)

def get_set_from_user(prompt):
    # Accepts a string input, splits it into elements, and converts it to a set of integers.
    user_input = input(prompt)
    return set(map(int, user_input.split()))

# Get input from the user for the first and second sets.
set_1 = get_set_from_user("Enter integers for the first set, separated by spaces: ")
set_2 = get_set_from_user("Enter integers for the second set, separated by spaces: ")

# Find the common elements (intersection) between the two sets.
common_elements = set_1 & set_2

# Display the result.
print(f"The common elements between the two sets are: {common_elements}")
