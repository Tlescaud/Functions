# Keyword arguments – learn how to use the keyword arguments


# specify the value of a parameter by name
# make function calls more readable and clear
# useful when functions have multiple parameters with default values
# or emphasize specific arguements in your funtion calls

# EXAMPLE.....

# Define a function with multiple parameters
def create_profile(name, age, city="Unknown", job="Unemployed"):
    profile = f"Name: {name}, Age: {age}, City: {city}, Job: {job}"
    return profile

# Using keyword arguments to call the function
profile1 = create_profile(name="Alice", age=30, city="New York", job="Engineer")
profile2 = create_profile(name="Bob", age=25)

# Print the results
print(profile1)  # Output: Name: Alice, Age: 30, City: New York, Job: Engineer
print(profile2)  # Output: Name: Bob, Age: 25, City: Unknown, Job: Unemployed


