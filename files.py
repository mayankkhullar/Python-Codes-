filename = "hello.txt"
file = open(filename, "r+")
lines = file.readlines()
for line in lines :
    print line
    if line!= "Heyy":
        file.write(line)
        print "done"
file.close()
