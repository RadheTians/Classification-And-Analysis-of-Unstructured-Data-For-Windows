import subprocess
import os
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)


def FileData(FilePath):
	seq=os.listdir(FilePath)
	#print(type(seq))
	#f = open("test.csv",'w')
	return seq


def MetaData(file_name):
	#file_name="test.csv"
	execution="C:/Fourth RadheTians/Project/Mini_Project_CS_240/Mini_Project/File_Metadata/Radhe data/exiftool.exe"
	production= subprocess.Popen([execution,file_name],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
	Data_Sets=[]
	for outer in production.stdout :
	    Data_Sets.append(outer)
	return Data_Sets

#list=FileData('C:/Files_Data_Set')
path=['C:/Files_Data_Set']
list=pool.map(FileData,path)
print(list)
value=[]
r=0
for listers in list:
	value.append(str(path[0])+str(list[r][r]))
	r+=1

print(value)

'''listener=pool.map(MetaData,value)
pool.close()
print(listener)'''

