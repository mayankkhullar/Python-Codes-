import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
print root.tag , root.attrib
# prints 
for child in root :
    print child.tag , child.attrib # prints child name and its attrib
    print 'ranks' , child.find('rank').text
#for child in root:
for country in root.findall("country"):
    rank = country.find('rank').text
    year = country.find('year').text
    #name = country.get('name')
    print  rank , year 
# iterate through the child's child element using root.iter method
for rank in root.iter('rank'):
     new_rank = int(rank.text) + 1
     rank.text = str(new_rank)
     rank.set('updated' , 'yes')
     print "written to file" , tree.write('output.xml')
