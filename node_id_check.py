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

root_dir = os.listdir(path)
root_dir.sort()	

#print len(root_dir)
if (os.path.isdir(path + root_dir[0])):
	for i in range (0, len(root_dir)):
		#print root_dir[i]
		curr_dir_path = path + root_dir[i]
		if (os.path.isdir(curr_dir_path)):
			curr_dir = os.listdir(curr_dir_path)
			curr_dir.sort()
			for j in range(0, len(curr_dir)):
				#print curr_dir[j]
				curr_node_id = curr_dir[j][:36]
				if check_node_id != curr_node_id:
					print "node id change in directory " + root_dir[i]
					print "\tfrom " + check_node_id
					print "\tto   " + curr_node_id
					check_node_id = curr_node_id
		
#print path + root_dir[0]

exit(0)