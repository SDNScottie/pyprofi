__author__ = 'sdnscottie'

import sqlite3
import os
import copy

from ipaddress import IPv4Address, IPv4Network

class cSQLite_ClientServerMgmt_App__ciud:
    global connection
    global cursor
    global sql_command

    def __init__(self, z_msg):

        PWD = os.path.realpath(os.path.dirname(__file__)) + "\\"

        #print("ABS_PATH = " + PWD )

        self.connection = sqlite3.connect(PWD+"database__clientservermgmt_app.db")
        self.cursor = self.connection.cursor()


    #====================================================================
    #== DROP table : ClientServerMgmt
    #====================================================================
    def drop_table__ClientServerMgmt(self):
        # delete
        self.cursor.execute("""DROP TABLE ClientServerMgmt;""")
        self.connection.commit()

    #====================================================================
    #== CREATE table : ClientServerMgmt_app_database.db
    #====================================================================
    def create_table__ClientServerMgmt(self):

        PWD = os.path.realpath(os.path.dirname(__file__)) + "\\"

        self.connection = sqlite3.connect(PWD+"database__clientservermgmt_app.db")
        #self.cursor = self.connection.cursor()

        self.connection.execute('CREATE TABLE ClientServerMgmt (cs_id INTEGER PRIMARY KEY AUTOINCREMENT,clientserver TEXT type UNIQUE,addr TEXT,city TEXT,ipsubnetaddress TEXT)')

        #==never forget this, if you want the changes to be saved:
        self.connection.commit()

    #====================================================================
    #== INSERT function
    #====================================================================
    def insert_row_of_data__into__ClientServerMgmt(self, z_clientserver, z_addr, z_city, z_ipsubnetaddress):

        insert_tuple_data = (
             #z_cs_id
             z_clientserver
            ,z_addr
            ,z_city
            ,z_ipsubnetaddress
        )		

        try:
            self.sql_command = """ INSERT INTO ClientServerMgmt(clientserver,addr,city,ipsubnetaddress) VALUES (?,?,?,?)"""
            self.cursor.execute(self.sql_command, insert_tuple_data)

            #==never forget this, if you want the changes to be saved:
            self.connection.commit()

        except sqlite3.Error as er:
            print ( 'er:' + str( er )  )

    #====================================================================
    #== DELETE function
    #====================================================================
    def delete_row_of_data__from__ClientServerMgmt(self, z_cs_id):

        cs_id = int(z_cs_id)
        print(" .... cs_id = " + str(cs_id))

        try:

            self.sql_command = " DELETE from ClientServerMgmt where cs_id = "+ str(cs_id) +" "
            print("sql = " + self.sql_command )
            self.cursor.execute(self.sql_command)

            print("performed: " + self.sql_command)

            #==never forget this, if you want the changes to be saved:
            self.connection.commit()

        except sqlite3.Error as er:
            #print ( 'er:' + str( er.message )  )
            print ( 'er:' + str( er )  )
            
    #====================================================================
    #== select/get data functions
    #====================================================================
    def select_all_data__ClientServerMgmt(self):

        cur = self.connection.cursor()
        cur.execute("select * from ClientServerMgmt")
        return cur.fetchall()

    def mylist(self):
        myl = []
        myl.append('1')
        return myl

    def get_six_col_table__w__verified_ipsubnetaddress_dynamic(self):
        
        #==========================
        #===( dynamic data )
        #==========================
        five_col_table = self.select_all_data__ClientServerMgmt()
        six_col_table = []
        for row in five_col_table:
            print(" 5column_table = " + str(row[4]) )
            #==========================#==========================
            #==Here is where tie calculation could be performed
            #==========================#==========================
            #my_ip_class = self.determine_SubnetClass_A_B_C("172.18.128.53/24")  #This was just for testing..
            my_ip_class = self.determine_SubnetClass_A_B_C(row[4])
            print(" tested ... my_ip_class = " + my_ip_class)
            
            my_ip_subnet_elements = row[4]
            print("my_ip_subnet_elements = " + str(my_ip_subnet_elements))
            
            six_col_table.append( [ str ( row[0] ) , str( row[1] ) , str( row[2] ) , str( row[3] ) , str( row[4] ) , my_ip_class ] )

        for row in six_col_table:
            print("resulting 6 column table : " + str(row) )

        print("specific element = " + str( six_col_table[0][1] ))

        return six_col_table


    def determine_SubnetClass_A_B_C(self, z_ip_address_slash_subnet):

        ip_address_elements = z_ip_address_slash_subnet.split("/")
        ip = str(ip_address_elements[0])
        subnet = str(ip_address_elements[1])
        print("..+..ip_address_elements = " + str(ip_address_elements) )
        print("..+..ip = " + ip)
        print("..+..subnet = " + subnet)

        """
        https://stackoverflow.com/questions/42385097/check-if-ip-address-belongs-to-a-class-a-b-and-c-in-python/42385606
        classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
        classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
        classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")

        To use it you will just check if a certain IPv4Address is in the IPv4Network as if you were checking in 
        an element is found inside a list:
        """
        
        classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
        classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
        classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")

        plausi_ip_address = IPv4Address(ip)     

        if plausi_ip_address in classA:
            return "Class-A"
        elif plausi_ip_address in classB:
            return "Class-B"
        elif plausi_ip_address in classC:
            return "Class-C"
        else:
            return "do not know"

    def close_connection(self):
        self.connection.close()


# ============================================================
# == Main
# ============================================================
def main():
    result = cSQLite_ClientServerMgmt_App__ciud("")
    
    #====================
    #==Step 1:
    #====================
    #result.create_table__ClientServerMgmt()

    #result.insert_row_of_data("7000300211","n7k-core2-BKN", "Eth5/8","link statistics","65044726", "c6506-bckp20.intern.zdf.de", "Gig6/1","link statistics", "WS-C6506-E", "10_192.168.178.33_24", "7000001038_650620200601000")
    #result.select_all_data__create__node_push("700030001", "n7k-core1-BKN")
    #====================
    #==Step 2:
    #====================
    #result.insert_row_of_data__into__ClientServerMgmt("N-9453","Mainz","Xdee Str.1","192.168.128.53/24")
    #result.insert_row_of_data__into__ClientServerMgmt("N-9463","Mainz","Xdee Str.1","192.168.128.63/24")
    #result.insert_row_of_data__into__ClientServerMgmt("N-9463A","Mainz","Xdee Str.1","128.0.0.0/16") #class b

    #====================
    #==Step 3:
    #====================
    #rows = result.select_all_data__ClientServerMgmt()
    #for row in rows:
    #    print( str ( row ) )
    #    print( str ( row[0] ) )

    #===dynamically create table with verified ipsubnetaddress code
    #six_col_table = result.get_six_col_table__w__verified_ipsubnetaddress_dynamic()
    #print("====print the result=====")
    #print(six_col_table)
    #for row in six_col_table:
    #    print( str(row) )

    #=========================================
    #==Perform some tests :
    #=========================================
    res = result.get_six_col_table__w__verified_ipsubnetaddress_dynamic()
    
    """
    classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
    classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
    classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")
    """
    #res = result.determine_SubnetClass_A_B_C("10.0.0.0/8")  #==must return classA
    #res = result.determine_SubnetClass_A_B_C("172.16.0.0/12")  #==must return classB
    #res = result.determine_SubnetClass_A_B_C("192.168.0.0/16")  #==must return classC
    #print(" ... tested IP/subnet = " + res)

    #====================
    #==Lastly:
    #====================

    #result.drop_table__SUBNETTING()   #~~drop table
    #result.create_table__SUBNETTING() #~~create table
    result.close_connection()

if __name__ == '__main__':
    main()
