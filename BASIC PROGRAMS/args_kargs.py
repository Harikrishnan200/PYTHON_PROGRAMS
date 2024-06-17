def print_args(*args):
    """This function prints all the arguments passed to it."""
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    """This function prints all the keyword arguments passed to it."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_args(1, 2, 3)
# Output:
# 1
# 2
# 3

print_kwargs(name="Alice", age=30)
# Output:
# name: Alice
# age: 30
