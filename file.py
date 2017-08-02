import shutil , re
files = open("hello.txt" , "r+")
print files.name
file = open("design.txt" , "r+")
for line in file:
    line = line.rstrip()
    #if line.startswith('java'):
    if re.search('^java' , line) :
        print  line
#String = file.read()
#print String
