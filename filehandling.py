def rawinputfile():
    inputfile = raw_input("Enterfile file name")
    files = open(inputfile)
    for x in files:
        print x
def readswithoutspace():
    file = open('abc.txt')
    for x in file:
        print x.strip()
def stringreadfromfile():
    file = open('abc.txt')
    y = file.read()
    print y[:5]

readswithoutspace()
stringreadfromfile()
rawinputfile()
    


