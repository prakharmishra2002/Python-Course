class MyClass:
    def __init__(self):
        self._private_variable = 10    # private variable
        
    def _private_method(self):    # private method
        return 'This is a private method'

obj = MyClass()  # Creating an object

# Accessing private members (not recommended but possible)
print(obj._private_variable)  # Output: 10
print(obj._private_method())  # Output: This is a private method