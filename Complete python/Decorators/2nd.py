def debug(func):
    def wrapper(*args, **kwargs):
        Devesh_value = ', '.join(str(value) for value in args)
        Shivam_value = ', '.join(f"{key} {value}" for key, value in kwargs.items())
        print(f"calling: {func.__name__} with Devesh {Devesh_value} and Shivam {Shivam_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="WoW"):
    print(f"{greeting}, {name}")
greet("chai", greeting="han ji")

hello()