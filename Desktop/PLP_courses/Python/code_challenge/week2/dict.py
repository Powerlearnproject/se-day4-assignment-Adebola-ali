# Create an empty dictionary to store the preson information.
person_info = {}

# Prompt the user for input and store it in the dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print(f"\n Hi {person_info['name']} Here is your information:")
print(person_info)

