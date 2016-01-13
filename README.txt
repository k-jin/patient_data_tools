Node ID Check

Usage:

node_id_check.py /path/to/src/

Summary:
This script finds all the node IDs in the root directory. The tool expects
a root directory with directories of binary files. Each of the directories
in the root is expected to be a separate day. The tool will print out any
changes in node ID it finds and which folder the change is found in, in 
the following format:

"""
node id change in directory <directory-name>
	from <original-node-id>
	to <new-node-id>
"""

Note: This script expects a node id 35 characters long 


Directory Copier

Usage: 

directory_copier.py /path/to/src/ /path/to/dst/

This script recursively copies the root folder, but ignoring any directory
named "backup" found on the relative path "plugins/vci-healthpath/data". 
The destination directory must not already exist.

Additionally, this script also writes a README file in the target directory.
This file will contain the name of the source directory.

Day Compressor

Usage: 

day_compressor.py /path/to/src/ /path/to/dst/

This script zips every directory within the source directory and writes the 
compressed directory to the destination directory. If there are files in 
source directory, those are compressed into an "other.zip" file.


