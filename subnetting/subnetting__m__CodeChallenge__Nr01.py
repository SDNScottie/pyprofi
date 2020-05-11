import os
import ipaddress


"""
SDNScottie CodeChallenges in Python3. Solutions will be in the 
associated method files. In this case the ( subnetting__m.py ) Happy CodeChallenge :-D
"""

__version__ = 'git'

import struct
import sys


IPV4LENGTH = 32
IPV6LENGTH = 128


class cSubnetType___CodeChallenge__Nr01:
    def __init__(self, ip_address, slash_mask):
        self.name = ip_address
        self.age = slash_mask      # slash_mask can be ( 8 thru 32 )
        #== perform test :
        #=1) take the ip_address and break it up into a ( List )
        List_ip_address = ip_address.split(".")

        #== Now, send the ( List ) into the individuals ( methods )
        #== and determine if class A, class B or class C IP address :-D

        if self.check_if_class_A(List_ip_address, slash_mask) == True:
            print("IP is a class A")
        elif self.check_if_class_B(List_ip_address, slash_mask) == True:
            print("IP is a class B")
        elif self.checkt_if_class_C(List_ip_address, slash_mask) == True:
            print("IP is a class C")


    def check_if_class_A(self, List_ip_address, slash_mask):
        print("check if class A : " + str(List_ip_address))
        result = True

        #== Tip: Here the goal is break compare the List members and 
        # determine if IP is class A

        return result

    def check_if_class_B(self, List_ip_address, slash_mask):
        print("check if class A : " + str(List_ip_address))
        result = True

        #== Tip: Here the goal is break compare the List members and 
        # determine if IP is class A

        return result

    def checkt_if_class_C(self, List_ip_address, slash_mask):
        print("check if class A : " + str(List_ip_address))
        result = True

        #== Tip: Here the goal is break compare the List members and 
        # determine if IP is class A

        return result

# ============================================================
# == MAIN
# ============================================================

def main_cSubnetType():
    cSubnetType___CodeChallenge__Nr01("192.168.0.0","16")

if __name__ == '__main__':
    main_cSubnetType()
