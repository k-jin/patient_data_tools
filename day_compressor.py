import os, sys, tarfile

if (len(sys.argv) != 3):
	print "usage: day_compressor.py /path/to/src/ /path/to/dest/"
	print "path should be path to the directory holding all the day directories"
	exit(0)

src_path = sys.argv[1]
dest_path  = sys.argv[2]

src_dir_files = os.listdir(src_path)

for i in range (0, len(src_dir_files)):
	curr_dir_path = src_path + src_dir_files[i]
	if (os.path.isdir(curr_dir_path)):
		curr_dir_files = os.listdir(curr_dir_files)
		curr_dir_files.sort()
		tar = tarfile.open(src_dir_files[i] + ".tar.gz", "w:gz")
		tar.add(curr_dir_path)
		tar.close()


