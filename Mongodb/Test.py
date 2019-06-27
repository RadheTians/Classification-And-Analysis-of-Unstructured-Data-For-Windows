import os
seq=os.listdir("C:/Users/Radhe Raman Tiwari/Anaconda3/Scripts/")
print(type(seq))
f = open("test.csv",'w')

for list in seq:
    print(list)
    f.write(list+'\n')

import win32com.client
sh=win32com.client.gencache.EnsureDispatch('Shell.Application',0)
ns = sh.NameSpace(r'C:\Users\Radhe Raman Tiwari\Desktop\ABTians.jpg')
colnum = 0
columns = []
while True:
    colname=ns.GetDetailsOf(None, colnum)
    if not colname:
        break
    columns.append(colname)
    colnum += 1

for item in ns.Items():
    print (item.Path)
    for colnum in range(len(columns)):
        colval=ns.GetDetailsOf(item, colnum)
        if colval:
            print('\t', columns[colnum], colval)

