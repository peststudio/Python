import os, sys
from stat import *
def get_filepath(directory):
	files = ""
	for name in os.listdir(directory):
		pathname = os.path.join(directory, name)
        	mode = os.stat(pathname).st_mode
		permission = oct(S_IMODE(mode))
		uid = os.stat(pathname).st_uid
		gid = os.stat(pathname).st_gid
		size = os.stat(pathname).st_size
		mtime = os.stat(pathname).st_mtime
		print permission, uid, gid, size, chr(9), mtime, name 
        return files
#print get_filepath("/home/lei/codes/Python")
if __name__ == '__main__':
    get_filepath(sys.argv[1])
