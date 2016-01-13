import os, sys, zipfile

# Currently compresses existing directories sorted by day

if (len(sys.argv) != 3):
	print "usage: day_compressor.py /path/to/src/ /path/to/dst/"
	print "path should be path to the directory holding all the day directories"
	exit(0)

src_path = sys.argv[1]
dest_path  = sys.argv[2]

src_dir_files = os.listdir(src_path)

other_files_bool = False

other_files = zipfile.ZipFile(dest_path + "other.zip", 'w', zipfile.ZIP_DEFLATED)
for i in range (0, len(src_dir_files)):
	curr_dir_path = os.path.join(src_path, src_dir_files[i])
	if (os.path.isdir(curr_dir_path)):
		curr_dir_files = os.listdir(curr_dir_path)
		curr_dir_files.sort()
		zipped = zipfile.ZipFile(dest_path + src_dir_files[i] + ".zip", 'w', zipfile.ZIP_DEFLATED)
		for j in range (0, len(curr_dir_files)):
			zipped.write(os.path.join(curr_dir_path, curr_dir_files[j]), curr_dir_files[j])
		zipped.close()
	else:
		other_files_bool = True
		other_files.write(curr_dir_path, src_dir_files[i])
other_files.close()

if not other_files_bool:
	os.remove(dest_path + "other.zip")