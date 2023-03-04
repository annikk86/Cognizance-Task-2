# Write a python program that reads the contents from the given file ‘onelinefile.txt’. 
# The file contains a single line which is of the format (int)(string)(float)(string) repeatedly. 
# Your main task is to split the contents of the given file based on their format and write it into a .csv file say ‘Filename2.csv’.

import re

f = open("onelinefile.txt")
data = f.read()
f.close()

exp = re.compile(r'(\d+)([A-Za-z]+)(\d+\.\d+)([A-Za-z]+)')
x = exp.findall(data)

f = open("Filename2.csv", "w")
for i in x:
    f.write(",".join(i) + "\n")
f.close()
