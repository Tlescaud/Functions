# define a function with default values for one or more parameters
# if caller doesnt provide value, default value will be used


# Function with default parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling the function with both parameters
greet("Alice", "Hi")  # Output: Hi, Alice!

# Calling the function with only the required parameter
greet("Bob")  # Output: Hello, Bob!


'''The greet function has two parameters: 

name (required) and greeting (with a default value of "Hello").

When the function is called with both parameters (greet("Alice", "Hi")), 

it uses the provided values and prints Hi, Alice!.

When the function is called with only the required parameter (greet("Bob")),

it uses the default value for greeting and prints Hello, Bob!.'''

# funtion with multiple default parameters

def calculate_total(price, tax=0.05, discount=0.10):
    total = price + (price * tax) - (price * discount)
    return total

# Calling the function with all parameters
print(calculate_total(100, 0.07, 0.15))  # Output: 92.0

# Calling the function with only the required parameter
print(calculate_total(100))  # Output: 95.0

# Calling the function with two parameters
print(calculate_total(100, 0.07))  # Output: 98.0

'''Summary:

Default parameters provide flexibility and make functions easier to use 

by allowing you to omit certain arguments when calling them. 

You can specify default values for one or more parameters 

and still override them if needed.

If you have any specific requirements or need further examples, 

feel free to let me know!
'''

