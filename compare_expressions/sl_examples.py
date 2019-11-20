import os

class cSL:

    def __init__(self, msgs=True):
        self.set_msgs(msgs)

    __msgs = None  # ~ private variable   ( those are best !! )
    def set_msgs(self, z_msgs):
        self.__msgs = z_msgs
    def get_msgs(self):
        return self.__msgs

    global myText
    myText = ""

    def information_about_cSL_class(self):
        if self.__msgs == True:
            myText = "List some Advantages of cSL : \n"
            print( myText )
            self.pwd_of_this_class()
        elif not self.__msgs == True:
            pass

    def tshoot_any__cSL___problem(self):
        print("tshoot_any__cSL___problem")

    def pwd_of_this_class(self):
        PWD = os.path.realpath(os.path.dirname(__file__))
        print("e.g. this classes location : " + PWD)
        return PWD

    def evenodd(self,x):
        if x % 2 == 0:
            print("Your digit is even")
        else:
            print("Your digit is odd")
    def primenumber(self,x):
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            print("Your digit is not a prime number")
        else:
            print("Your digit is  a prime number")
    def squareroot(self,x):
        y = x ** 0.5
        print("The square root is " + str(y))
    def squarenumber(self,x):
        sn = x * x
        print("The square number is " + str(sn))
    def sumdigits(self,x):
        sod = 0
        z = x
        while z:
            sod += z % 10
            z = int(z / 10)
        print("The sum of digits is " + str(sod))
    def divider(self,x):
        teiler = [1]
        count = 2
        while x + 1 > count:
            if x % count == 0:
                teiler.append(count)
            count += 1
        print("Divider from " + str(x) + str(teiler))


# ============================================================
# == main, program starts here
# ============================================================
def main():

    res = cSL(msgs=True)
    #res.information_about_cSL_class()

    print("Please enter a digit between 0 and 1000")
    x = int(input())
    while x > 1000 or x < -1:
        if x > 1000 or x < -1:
            print("Please enter a digit between 0 and 1000")
            x = int(input())
    res.evenodd(x)
    res.primenumber(x)
    res.squareroot(x)
    res.squarenumber(x)
    res.sumdigits(x)
    res.divider(x)


if __name__ == '__main__':
    main()
