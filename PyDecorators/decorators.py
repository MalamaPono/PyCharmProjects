# A Decorator is simply a function that takes another function as an argument, adds some kind of
# functionality and then finally returns another function. Doing this all without altering the source
# code of the original function that was passed in.

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display fucntion ran')

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

# display = decorator_function(display) #this line is the same as if you put the @decorator_function
display()                             #decorator above the display function
display_info('John',25)