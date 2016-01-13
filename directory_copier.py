import sys, os, shutil

# https://docs.python.org/2/library/shutil.html

if (len(sys.argv) != 3):
	print "usage: directory_copier.py /path/to/src/ /path/to/patient/"
	print "patient folder must not exist"
	exit(0)

src_path = sys.argv[1]
dst_path = sys.argv[2]

backup_path = 'plugins/vci-healthpatch/data'

print os.path.join(src_path, backup_path)

shutil.copytree(src_path, dst_path,
              ignore=lambda p,f: ['backup'] if p == os.path.join(src_path, backup_path) else [])

f = open(os.path.join(dst_path, 'README.txt'), 'w')
f.write("Device ID: " + os.path.split(os.path.split(src_path)[0])[1])
f.close()
# recursive_copy(sys.argv[1], sys.argv[2])




# def recursive_copy(src, dest):
# 	for root, dirs, files in os.walk(src):
# 		for dir_name in dirs:
# 			if "backup" not in dir_name:
# 				os.mkdir(os.path.join(dest, dir_name))
# 				recursive_copy(os.path.join(src, dir_name), os.path.join(dest, dir_name))
# 		for file_name in files:


