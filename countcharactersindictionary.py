counts = dict()
names = ['a' , 'b' , 'b' , 'c' ]
for name in names:
    counts[name] = counts.get(name , 0) + 1
print counts
    
