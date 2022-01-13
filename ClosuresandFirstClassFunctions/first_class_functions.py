# First Class Functions:
"A programming language is said to have first-class functions if it treats its functions as first-class citizens"

# First Class Citizen:
"""A first class citizen (sometimes called first-class objects) in a programming language is an entity which
supports all the operations generally available to other entities. These operations typically include being
passed in as an argument, returned from a function, and assigned to a variable"""

def square(x):
    return x*x

def my_map(func, lis):
    new_lis = []
    for num in lis:
        new_lis.append(func(num))
    return new_lis

f = square
new_lis = my_map(f,[1,2,3,4])
print(new_lis)

def html_tag(tag):

    def wrap_text(msg):
        return '<{0}>{1}<{0}/>'.format(tag,msg)

    return wrap_text

h1 = html_tag('h1')
message1 = h1('This is wrapped in h1')
message2 = h1("Wrap this is h1 tag as well")
print(message1,message2)