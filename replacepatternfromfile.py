import cx_Oracle
file = open("design.txt")
str = file.read()
#print str
x = str.replace("#java.heap.size.initial=128M" , "#java.heap.size.initial=118M" , 1)
y = str.replace("java.library=%TIBCO_JVM_LIB_SERVER%" , "Mayank" , 1)
print x ,y
