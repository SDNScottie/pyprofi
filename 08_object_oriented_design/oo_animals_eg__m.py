__author__ = 'pyprofi'

#ref: http://www.python-kurs.eu/klassen.php

import sys, os
parent_dir = os.getcwd() # find the path to module a
#==Then go up one level to the common parent directory
PWD = os.path.realpath(os.path.dirname(__file__))

path = os.path.dirname(parent_dir)
#==Add the parent to sys.pah
sys.path.append(os.getcwd() )
sys.path.insert(0,PWD+"//*")

from animal.animal__m import cCat
from animal.animal__m import cDog

class cAnimals_eg(object):

    def __init__(self):

        parent_dir = os.getcwd() 
        #print("parent_dir = " + parent_dir)

        PWD = os.path.realpath(os.path.dirname(__file__))
        #print("PWD = " + PWD)

        #print(" full python path = " + str(sys.path))

        c = cCat()
        print( str( c.make_a_sound() ) )

        d = cDog()
        print( str( d.talk() ))


if __name__ == "__main__":
    print("\ncAnimals is being run directly")
    main = cAnimals_eg()
else:
    print("\cAnimals_eg is being imported into another module")
