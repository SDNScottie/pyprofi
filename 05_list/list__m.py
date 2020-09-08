__author__ = 'sdnscottie'


import sys

sys.path.append("C:\\Users\\yourUserName\\yourPythonProjectDirectory\\")


import os

import shutil
from pyometry.date_time.date_time__m import cDate_Time

class cList:

    def __init__(self, msgs=True):
        self.set_msgs(msgs)

    __msgs = None  # ~ private variable   ( those are best !! )
    def set_msgs(self, z_msgs):
        self.__msgs = z_msgs
    def get_msgs(self):
        return self.__msgs

    def pwd_of_this_class(self):
        PWD = os.path.realpath(os.path.dirname(__file__))
        print("e.g. this file's location : " + PWD)
        return PWD

    def append_a_list__return_list(self):
        myl = []
        myl.append('1')

        print("result of list = " + str(myl))
        return myl

    def append_multidimensional_list(self):
        a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
        
        for record in a:             
            print("record = " + str(record)) 

        for record in a:  
            record.append("new element")           
            print("record = " + str(record)) 

        for record in a:  
            record.append(60)           
            print("record = " + str(record)) 


    def add_a_sublist_to_a_multidimensional_list(self):
        a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 

        for record in a:             
            print("1)record = " + str(record)) 

        a.append([5, 10, 15, 20, 25]) 
        for record in a:             
            print("2)record = " + str(record)) 

        a.append([5, 10, 15, 'a string val', 55]) 
        a.append([5, 10, 15, 'another string val', 65]) 
        for record in a:             
            print("3)record = " + str(record)) 

    def access_the_first_elements_in_the_sublist(self):
        a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 

        a1 = [ i[0] for i in a ]

        print(a1)


    def access_a_list_of_lists(self):
        data = [ [1, 2, 3, 4]
                ,['blue', 'green', 'red', 'yellow'] 
                ,['yellow0', 'yellow1', 'yellow2', 'yellow3'] 
               ]

        data.append( ['elephant', 'donkey', 'cat'] )
        data.append( ['cat', 'black', 'long ears'] )

        #for record in data:
        print("result of data = " + str(data))

        print("a)specific records element = " + str( data[0] ) )

        print("b)specific records element = " + str( data[1][2] ) )


    def ip_subnet_elements_list(self):
        ip_subnet = [ ['192.168.178.4/24']
                     ,['192.168.21.7/24']
                    ]
        for record in ip_subnet:
            print(record)

            #subnet_elements = str(record).split("/")
            #print("subnet_elements = " + str(subnet_elements).replace("'",""))
            #print("subnet_elements[ip] = " + str(subnet_elements[0]))


        #words = text.split(",") 


# ============================================================
# == Main
# ============================================================
def main():

    res = cList(msgs=True)

    #res.append_a_list__return_list()

    #res.append_multidimensional_list()

    #res.add_a_sublist_to_a_multidimensional_list()

    #res.access_the_first_elements_in_the_sublist()

    #res.access_a_list_of_lists()

    res.ip_subnet_elements_list()

if __name__ == '__main__':
    main()
