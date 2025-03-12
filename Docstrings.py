'''using docstrings in python.........

Docstrings in Python are used to document modules, functions, classes, and methods.
They provide a convenient way to include descriptions and explanations of the code,
making it easier for others (and yourself) to understand and maintain the code later.

Here's how to use docstrings in Python:'''


def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b


# Accessing the docstring
print(add.__doc__)



# example 2: class docstring

class Dog:
    """
    A class to represent a dog.

    Attributes:
    name (str): The name of the dog.
    age (int): The age of the dog.

    Methods:
    bark(): Prints a message indicating the dog is barking.
    """

    def __init__(self, name, age):
        """
        Initialize the dog with a name and age.

        Parameters:
        name (str): The name of the dog.
        age (int): The age of the dog.
        """
        self.name = name
        self.age = age

    def bark(self):
        """
        Print a message indicating the dog is barking.
        """
        print(f"{self.name} is barking.")


# Accessing the docstring
print(Dog.__doc__)
print(Dog.bark.__doc__)






'''Explanation: 

Function Docstring: The docstring for the add function describes what the function does, its parameters, and the return value.

Class Docstring: The docstring for the Dog class provides an overview of the class, its attributes, and methods.

Accessing Docstrings: You can access docstrings using the __doc__ attribute of the function, class, or method.

Docstring Conventions
Triple Quotes: Docstrings are enclosed in triple quotes (""" or '''
'''
), allowing them to span multiple lines.

PEP 257: Follow the PEP 257 conventions for writing docstrings to ensure consistency and readability.

Summary
Docstrings are a valuable tool for documenting your Python code, providing clear explanations and descriptions of modules, 

functions, classes, and methods. They make your code more readable and maintainable, especially when collaborating with others
 
 or revisiting your own code after some time.

If you have any specific questions about using docstrings or need further examples, let me know!'''