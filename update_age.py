import datetime

# Your birthdate (update it accordingly)
birthdate = datetime.datetime(2003, 1, 8)  # Example: January 8, 2003

# Get the current date
current_date = datetime.datetime.now()

# Calculate the new age based on the current date
new_age = current_date.year - birthdate.year
if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
    new_age -= 1  # If the birthday hasn't occurred yet this year, subtract 1

# Read the README file
with open('README.md', 'r') as file:
    content = file.read()

# Replace the age in the README
new_content = content.replace(f'self.age = {new_age - 1}', f'self.age = {new_age}')

# Write the updated content back to the README file
with open('README.md', 'w') as file:
    file.write(new_content)

print(f"Age updated to {new_age}")
