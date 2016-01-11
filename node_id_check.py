import sys,os

# path should be path to the directory holding all
# directories of each day

if (len(sys.argv) != 2):
	print "usage: node_id_check.py /path/to/src/"
	print "path should be path to the directory holding all the day directories"
	exit(0)

path = sys.argv[1]
check_node_id = ""
curr_node_id = ""

root_dir_files = os.listdir(path)
root_dir_files.sort()	

#print len(root_dir)

for i in range (0, len(root_dir_files)):
	#print root_dir[i]
	curr_dir_path = os.path.join(path, root_dir_files[i])
	if (os.path.isdir(curr_dir_path)):
		curr_dir_files = os.listdir(curr_dir_path)
		curr_dir_files.sort()
		for j in range(0, len(curr_dir_files)):
			#print curr_dir[j]
			curr_node_id = curr_dir_files[j][:36]
			if check_node_id != curr_node_id:
				print "node id change in directory " + root_dir_files[i]
				print "\tfrom " + check_node_id
				print "\tto   " + curr_node_id
				check_node_id = curr_node_id
		
#print path + root_dir[0]

exit(0)