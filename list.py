import os, sys, time
import stat 
import pwd
import grp 

def list_files(directory):
	for name in os.listdir(directory):
		pathname = os.path.join(directory, name)
		path_stat = os.stat(pathname)
        	mode = path_stat.st_mode
		permission = oct(stat.S_IMODE(mode))
		isdir = stat.S_ISDIR(mode)
		if isdir == 1:
			d = 'd'
		else:
			d = '-'
		fpermission = format_permission(permission)
		fpermission = d + fpermission
		uid = path_stat.st_uid
		uname = pwd.getpwuid(uid)
		gid = os.stat(pathname).st_gid
		gname = grp.getgrgid(gid)
		size = path_stat.st_size
		mtime = path_stat.st_mtime
		ftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
		print fpermission, uname.pw_name, gname.gr_name, size, '\t', ftime, name

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
