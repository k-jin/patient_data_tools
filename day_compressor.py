import os, sys

if (len(sys.argv) != 3):
	print "usage: day_compressor.py /path/to/src/ /path/to/dest/"
	print "path should be path to the directory holding all the day directories"
	exit(0)

src_path = sys.argv[1]