# Matthew Hall
# September 11, 2024
# String Concatenation

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in
city = "Traverse City, "
state = 'Michigan '
print(city + state)

# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
# Create another variable that stores the welcome message
# Use concatenation to create the customized message
message = "Welcome to my game, "
first_name = input('please enter your first name\n')
print(message + first_name)

# Part 3
# Assign a number to your age variable
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
# Use concatenation to display a sentence that tells us your first name and age
age = 16
age_2 = 17
message = "Hi, my name is "
message_2 = " I am "
message_3 = " but I ame turning "
message_4 = " in three days"
print(message + first_name + message_2 + str(age) + message_3 + str(age_2) + message_4 + ".")

# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches
height = 70
print(f'{first_name} has a height of {height} inches.')