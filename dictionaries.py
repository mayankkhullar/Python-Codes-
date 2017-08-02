def dictconstructor():
    dictionary = dict()
    dictionary['a'] = 12
    dictionary['b'] = 15

    print dictionary['a']
    x = int(dictionary['a'] + 1)
    print x
def createDict():
    dictionary = {'name' : 'Mayank' , 'Age' : 20 , 'DOB' : 20091993}
    #print values for key in dictionary.itervalues() :
    print dictionary.items()
dictconstructor()
createDict()
