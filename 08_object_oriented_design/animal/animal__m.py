
from abc import ABC, ABCMeta, abstractmethod

"""
https://stackoverflow.com/questions/3724110/practical-example-of-polymorphism
https://zaiste.net/posts/abstract_classes_in_python/


In user defined base classes, abstract methods should raise this exception 
when they require derived classes to override the method, or while the class 
is being developed to indicate that the real implementation still needs to be added.

"""

class cAnimal(ABC):   

    @abstractmethod
    def talk(self):       # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def make_a_sound(self): pass
        #raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def movement(self): pass
        #raise NotImplementedError("Subclass must implement abstract method")


class cCat(cAnimal):
    #def talk(self):
    #    return 'Meow!'
    def say_something(self):
        s = super(Cat, self).make_a_sound()
        #return "%s - %s" (s, "Miauuuuuuu 3")
        return s
    def talk(self):
        return 'Cat talks !!'

    def make_a_sound(self):
        return "Miauuu, I'm a cat"

    def movement(self):
        #m = super(Cat, self).movement()
        return "Cat is moving"

class cDog(cAnimal):
    def talk(self):
        return 'Woof! Woof!'

    def make_a_sound(self):
        return "Dog makes a sound"

    def movement(self):
        #m = super(Dog, self).movement()
        return "Dog is moving"        
