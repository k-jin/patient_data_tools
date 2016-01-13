import sys, os, shutil

if (len(sys.argv) != 3):
	print "usage: directory_copier.py /path/to/src/ /path/to/patient/"
	print "patient folder must not exist"
	exit(0)

src_path = sys.argv[1]
dst_path = sys.argv[2]

backup_path = os.path.normcase('plugins/vci-healthpatch/data')

shutil.copytree(src_path, dst_path,
              ignore=lambda p,f: ['backup'] if p == os.path.join(src_path, backup_path) else [])

f = open(os.path.join(dst_path, 'README.txt'), 'w')
f.write("Device ID: " + os.path.split(os.path.split(src_path)[0])[1])
f.close()