import pandas as pd
import numpy as np

file = 'bitbnsBuySale.csv'
# Reading the csv file
file1 = pd.read_csv('bitbnsBuySale.csv')
#print(str(file1))
if '.' in file:
    x1 =file.index('.')
    x2 = file[:file.index('.')]
    print(x2)
name = x2
filename = "%s.xlsx" % name
# saving xlsx file
GFG = pd.ExcelWriter(filename)
file1.to_excel(GFG, index = False)

GFG.save()
#print('Names2.xlsx')
