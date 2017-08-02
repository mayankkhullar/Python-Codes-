# Python code to demonstrate working of
# clear() and copy()
 
# Initializing dictionary
dic1 = { 'Name' : 'Nandini', 'Age' : 19 , 'ames' : 'Mayank' , 'Ages' : '12' }
print dic1.items()
# Initializing dictionary 
dic3 = {}
 
# using copy() to make shallow copy of dictionary
dic3 = dic1.copy()
 
# printing new dictionary
print ("The new copied dictionary is : ")
print (dic3.items())
 
for k, v in dic1.items():
	    print(k,v)
