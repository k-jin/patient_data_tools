import sys, os

# https://docs.python.org/2/library/shutil.html

if (len(sys.argv) != 3):
	print "usage: directory_copier.py /path/to/src/ /path/to/patient/"
	exit(0)

recursive_copy(sys.argv[1], sys.argv[2])




def recursive_copy(src, dest):
	for root, dirs, files in os.walk(src):
		for name in dirs:
			if (name != backup):
				os.mkdir(os.path.join(dest, name))
				recursive_copy(os.path.join(src, name), os.path.join(dest, name))
		for name in files:


