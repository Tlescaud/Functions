# define anonymous functions in python using lambda expressions

# useful for creating small, single-use functions without formally defining them using def

# tuple is a collection of data type in python
# that allows you to store multiple iteams
# in a single variable and data remains constant and unchanged

# Creating a tuple
my_tuple = (1, "apple", 3.14, [5, 6], (7, 8))

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: apple
print(my_tuple[3])  # Output: [5, 6]
print(my_tuple[4])  # Output: (7, 8)

# Trying to modify an element (will raise an error)
# my_tuple[1] = "banana"  # TypeError: 'tuple' object does not support item assignment


# example of lambda.......

# List of tuples
data = [(1, 4), (3, 2), (5, 1), (4, 3), (2, 5)]

# Sort the list using a lambda expression as the key
sorted_data = sorted(data, key=lambda x: x[1])

# Print the sorted list
print(sorted_data)  # Output: [(5, 1), (3, 2), (4, 3), (1, 4), (2, 5)]

'''Explanation
lambda x: x[1]: The lambda expression takes an argument x (each tuple in the list)
and returns the second element (x[1]) to be used as the sorting key.

sorted(data, key=lambda x: x[1]): The sorted() function uses the lambda expression
to sort the list based on the second element of each tuple.'''


