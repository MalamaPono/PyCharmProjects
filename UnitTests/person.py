class Person:

    age_multiplier = 1.5

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'My name is {} and I am {} years old.'.format(self.name,self.age)

    def getMultipliedAge(self):
        return self.age * self.age_multiplier