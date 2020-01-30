datafile = open("data.txt","r")
outFile = open("newdata.txt","w")
content = datafile.readlines()
content =[x.strip() for x in content]
#datafile.close()

nextRecord = []
for x in content:
    nextRecord.extend(x.split('\n'))
#print(any(c in nextRecord[0] for c in 'Salaries'))
#if 'Salary' in nextRecord[0]:
    #print('Succes')

#s = 'start'
#newRec =[]
#value = 0
#while s != '':
    #s = datafile.readline()
    #newRec.append(s.strip())
    #if 'DocID' in s:
        #print(s.split())
    #else:
        #print('no')
import pandas as pd
import numpy as np

frame = pd.DataFrame(content)
print(frame)
frame.to_json(outFile)
outFile.close()
datafile.close()
input("press any key to exit")
