from time import gmtime, strftime
import datetime

class cTime:

    def __init__(self, z_msg=True):

    def get_TS(self):

        ts = strftime("%Y") + "_" + strftime("%m%d") + "_" + strftime("%H%M%S")

        #print("TS:  " + strftime("%Y") + "_" + strftime("%m%d") + "_" + strftime("%H%M%S") + "\n\n")

        return ts

    def get_TS__justNrs(self):

        ts = strftime("%Y") + "_" + strftime("%m%d") + "_" + strftime("%H%M%S")

        return ts

    def format_time(self):
        t = datetime.datetime.now()
        s = t.strftime('%Y_%m%d_%H%M_%S.%f')
        tail = s[-7:]
        f = round(float(tail), 3)
        temp = "%.3f" % f
        return "%s%s" % (s[:-7], temp[1:])

    def split_time_into_list(self, z_string, z_split_at_char ):
        y_data_to_list = z_string.strip().split( z_split_at_char )
        y_list = list(y_data_to_list)
        print(y_list)

        self.set_year( str(y_list[2]) )
        return y_list

    global year
    def set_year(self, z_year):
        year = z_year
        print( " global year = " + year )

# ============================================================
# == Main
# ============================================================
def main():
    print( cTime(" ").get_TS__justNrs() )

    #print( cTime(z_msg=True).split_time_into_list("20.02.2017",".") )

if __name__ == '__main__':
    main()
