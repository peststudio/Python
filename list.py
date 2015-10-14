import os, sys, time
from stat import *
def get_filepath(directory):
	for name in os.listdir(directory):
		pathname = os.path.join(directory, name)
        	mode = os.stat(pathname).st_mode
		permission = oct(S_IMODE(mode))
		uid = os.stat(pathname).st_uid
		gid = os.stat(pathname).st_gid
		size = os.stat(pathname).st_size
		mtime = os.stat(pathname).st_mtime
		ftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
		print permission, uid, gid, size, chr(9), ftime, name 
if __name__ == '__main__':
    get_filepath(sys.argv[1])
