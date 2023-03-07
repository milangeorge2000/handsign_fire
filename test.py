
import os
import re

# Replace the first digit in each file with 'X'
def replace_first_digit(filename):
    with open(filename, 'r') as f:
        text = f.read()

    # Use a regular expression to find the first digit
    match = re.search(r'\d', text)
    if match:
        # Replace the first digit with 'X'
        text = text[:match.start()] + "9" + text[match.end():]

    with open(filename, 'w') as f:
        f.write(text)

# Iterate through all the files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        replace_first_digit(filename)
