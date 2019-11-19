
from abc import ABCMeta, abstractmethod

"""
https://stackoverflow.com/questions/3724110/practical-example-of-polymorphism
https://zaiste.net/posts/abstract_classes_in_python/

"""

class Animal:
    __metaclass__ = ABCMeta

    #def __init__(self, name):    # Constructor of the class
    #    self.name = name

    def __init__(self):    # Constructor of the class
        #self.name = name
        print("constructor : Animal")

    #def talk(self):              # Abstract method, defined by convention only
    #    raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def make_a_sound(self): pass

    @abstractmethod
    def movement(self): pass


class Cat(Animal):
    #def talk(self):
    #    return 'Meow!'
    def say_something(self):
        s = super(Cat, self).make_a_sound()
        #return "%s - %s" (s, "Miauuuuuuu 3")
        return s

    def make_a_sound(self):
        return "Miauuu, I'm a cat"

    def movement(self):
        m = super(Cat, self).movement()

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'