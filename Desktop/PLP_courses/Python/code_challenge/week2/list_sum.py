# Program to create a list of integers and compute their sum

# Accept user input and create a list of integers
user_inputs = input("Enter a list of integers separated by spaces: ")
integer_list = [int(x) for x in user_inputs.split()]

# Compute the sum of the integers in the list
list_sum = sum(integer_list)

# Print the result
print(f"The sum of the integers in the list is: {list_sum}")
