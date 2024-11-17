# List of words
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

# List comprehension to filter words with an odd number of characters
words_with_odd_length = [word for word in words if len(word) % 2 != 0]

# Print the result
print("Words with an odd number of characters:", words_with_odd_length)
