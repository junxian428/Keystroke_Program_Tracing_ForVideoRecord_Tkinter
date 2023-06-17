from collections import Counter

# Define the file path
file_path = "keystrokes.txt"

# Initialize a counter to store the frequency of each alphabet
frequency_counter = Counter()

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the file line by line
    for line in file:
        # Iterate over each character in the line
        for char in line:
            # Check if the character is an alphabet
            if char.isalpha():
                # Increment the count for the character
                frequency_counter[char.lower()] += 1

# Print the frequency of each alphabet
for alphabet, count in frequency_counter.items():
    print(f"Alphabet '{alphabet}' occurs {count} times.")