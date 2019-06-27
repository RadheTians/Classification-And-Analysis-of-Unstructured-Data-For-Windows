import os, time
from stat import * # ST_SIZE etc
file='test.csv'

try:
    st = os.stat(file)
except IOError:
    print("failed to get information about", file)
else:
    print("file size:", st[ST_SIZE])
    print("file size:", st[ST_MODE])
    print("file modified:", time.asctime(time.localtime(st[ST_MTIME])))

