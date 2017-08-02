from os import listdir
from os.path import isfile, join
import xlwt
import xlrd
f = open("words.txt", 'r+')
row_list = []
for row in f:
        row_list.append(row.split('|'))
print "ROW" , row_list   
column_list = zip(*row_list)
print "Column" , column_list
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
i = 0 
for column in column_list:
        for item in range(len(column)):
            worksheet.write(item, i, column[item])
        workbook.save(join('generated_xls' + str(i) + '.xls'))
        i+=1
