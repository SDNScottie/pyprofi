import os

class cLS:

    def __init__(self, msgs=True):
        self.set_msgs(msgs)

    __msgs = None  # ~ private variable   ( those are best !! )
    def set_msgs(self, z_msgs):
        self.__msgs = z_msgs
    def get_msgs(self):
        return self.__msgs

    global myText
    myText = ""

    def information_about_cLS_class(self):
        if self.__msgs == True:
            myText = "List some Advantages of cLS : \n"
            print( myText )
            self.pwd_of_this_class()
        elif not self.__msgs == True:
            pass

    def tshoot_any__cLS___problem(self):
        print("tshoot_any__cLS___problem")

    def pwd_of_this_class(self):
        PWD = os.path.realpath(os.path.dirname(__file__))
        print("e.g. this classes location : " + PWD)
        return PWD


# ============================================================
# == main, program starts here
# ============================================================
def main():

    res = cLS(msgs=True)
    res.information_about_cLS_class()

if __name__ == '__main__':
    main()
