# this decorator class has the same functionality as the decorator methods above. These examples
# just show how decorators are used with classes as this often seen many times in python.
class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call executed before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print('display fucntion ran')

@DecoratorClass
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

display()
display_info('John', 25)