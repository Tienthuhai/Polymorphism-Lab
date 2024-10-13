def execute(func, *args):
    """Execute the given function with the provided arguments."""
    return func(*args)

# Example functions
def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")

def say_bye(name):
    print(f"Bye, {name}")

# Test code
execute(say_hello, "Peter", "George")  # Output: Hello, Peter, I am George
execute(say_bye, "Peter")               # Output: Bye, Peter
