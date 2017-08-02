from datetime import datetime
import time , os
def fileexistence():
    x = os.path.isfile('abcd.txt')
    if x is True:
        file = open('abc.txt')
        for x in file:
                print x.strip()
    else:
         print 'file not found!!!!'

#def setFlag():
    #flags = os.UF_IMMUTABLE
    #os.chflags('abc.txt' , flags)
    #print 'flag set!!!!'

fileexistence()

#setFlag()






timestamp = 1226527167.595983
dt_obj = datetime.fromtimestamp(timestamp)
print repr(dt_obj)

dt_obj = datetime(2008, 11, 10, 17, 53, 59)
date_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
print date_str
print time.time()
