string='File Name                       : MP3'
list='File Modification Date/Time     : 218:012:19 17:41:27+05:30'
s=''
strings=list.split(':')
print(strings)
string=strings[0]
for x in strings[1:]:
    s=s+x+':'

splits = []
pos = -1
last_pos = -1
while ' ' in string[pos + 1:]:
    pos = string.index(' ', pos + 1)
    if string[last_pos+1:pos]!='':
        splits.append(string[last_pos + 1:pos])
    last_pos = pos

splits.append(string[last_pos + 1:])
splits.append(s)
print(splits)
print(splits[0]+' '+splits[1])
print(splits[-1])
dist={'1':'17010','2':'115'}
print(dist)
lister=list(dist)
print(lister)