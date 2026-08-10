from functools import wraps
# wraps is used to preserve the original function's metadata 
# when you replace it with a wrapper function.
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chai code")

greet()    

print(greet.__name__)