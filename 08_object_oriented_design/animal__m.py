__author__ = 'pyprofi'

#ref: http://www.python-kurs.eu/klassen.php

import sys, os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)
# Add the parent to sys.pah
sys.path.append(path)

#from pyometry.pyprofi.oop.animal.animals__m import *

class cAnimal(object):

    def __init__(self):

        print ("\nconstructor : Animals__main")

        d = Dog()
        d.make_a_sound()

        c = Cat()
        print( c.say_something() )
        print( c.make_a_sound() )
        print( c.movement() )

if __name__ == "__main__":
    print("\ncAnimal is being run directly")
    main = cAnimal()
else:
    print("\ncAnimal is being imported into another module")
