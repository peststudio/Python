import os, sys, time
from stat import *
from pwd import getpwnam, getpwuid

def list_files(directory):
	for name in os.listdir(directory):
		pathname = os.path.join(directory, name)
        	mode = os.stat(pathname).st_mode
		permission = oct(S_IMODE(mode))
		isdir = S_ISDIR(mode)
		if isdir == 1:
			d = 'd'
		else:
			d = '-'
		fpermission = format_permission(permission)
		fpermission = d + fpermission
		uid = os.stat(pathname).st_uid
		uname = getpwuid(uid)
		#gid = os.stat(pathname).st_gid
		#gname = getpwuid(gid)
		size = os.stat(pathname).st_size
		mtime = os.stat(pathname).st_mtime
		ftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
		print fpermission, uname.pw_name, size, chr(9), ftime, name 

def format_permission(permission):
	int_perm = int(permission)
	user = int_perm / 100
	grp = (int_perm / 10) % 10
	oth = (int_perm) % 10
	perm = format_part(user)
	perm = perm + format_part(grp)
	perm = perm + format_part(oth)
	return perm

def format_part(user):
	perm = ""
	if user > 3:
		perm += 'r'
	else:
		perm += '-'
	if user == 2 or user == 3 or user == 6 or user == 7:
		perm += 'w'
	else:
		perm += '-'
	if user % 2 == 1:
		perm += 'x'
	else:
		perm += '-'
	return perm

if __name__ == '__main__':
    list_files(sys.argv[1])
