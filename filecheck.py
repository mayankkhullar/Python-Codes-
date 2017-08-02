import os  
x = os.path.isfile('abcd.txt')
if x is True:
    file = open('abc.txt')
    for x in file:
        print x.strip()
else:
    print 'file not found!!!!'
