import subprocess
import os
import pymongo


def FileData(FilePath):
	seq=os.listdir(FilePath)
	return seq


def MetaData(file_name):
	execution="exiftool.exe"
	production= subprocess.Popen([execution,file_name],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
	Data_Sets=[]
	for outer in production.stdout :
	    Data_Sets.append(outer)
	return Data_Sets



def FileExtension(file):
	File=file
	NameWithExtension=File.split('.')
	fileName=NameWithExtension[-1].upper()
	FileName='File Type                       : '+fileName
	return FileName


def MongoData(FileList):

	Mongodb=[]
	List=FileList
	for lister in List:
		if lister.find('File Name')!=-1 or lister.find('File Type')!=-1 or lister.find('File Modification Date/Time')!=-1 or lister.find('File Access Date/Time')!=-1 or lister.find('File Creation Date/Time')!=-1:
			Mongodb.append(lister)
	Data_list=SetDataSet(Mongodb)
	return Data_list


def MongoConnect(mongolist,type):
	myclient = pymongo.MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox-ady7r.mongodb.net')

	mydb = myclient["FileCollection"]
	mycol = mydb[type+'FILES']
	list=[]
	list.append(mongolist)
	result=mycol.insert_many(list)
	return True

def SetDataSet(Listvalue):
	JSON={}
	keys=[]
	values=[]
	ListSet=Listvalue
	for i in range(0,5,1):
		listFile=StringSplit(ListSet[i])
		first=listFile[0]+' '+listFile[1]+' '+ listFile[2]
		last=listFile[-1]
		keys.append(first)
		values.append(last)
		JSON=dict(zip(keys, values))
		if first=='File Type ':
			MongoConnect(JSON,last)
	return values


def StringSplit(Strings):
	s=''
	list=Strings.split(':')
	string=list[0]
	for x in list[1:]:
		s=s+x+' '
	splits = []
	pos = -1
	last_pos = -1
	while ' ' in string[pos + 1:]:
		pos = string.index(' ', pos + 1)
		if string[last_pos + 1:pos] != '':
			splits.append(string[last_pos + 1:pos])
		last_pos = pos

	splits.append(string[last_pos + 1:])
	splits.append(s)
	return splits


def Main(FilePath):
	FullData=[]
	list=FileData(FilePath)
	for listprint in list:
		FullSet = []
		pinters=MetaData(FilePath+'/'+listprint)
		for pinter in pinters:
			if pinter.find('Error')!=-1:
				for pinter in pinters:
					if pinter.find('File Name')!=-1:
						filename=FileExtension(pinter[34:])
						FullSet.append(filename)

			else:
				FullSet.append(pinter)
		Data_Taken=MongoData(FullSet)
		FullData.append(Data_Taken)

	return FullData

if __name__ == "__main__":
	Main()

