#!/usr/bin/env python

import os

def convert_dos_file_endings_to_unix_in_these_directories(used_directory):

	os.system("apt-get install dos2unix")

	for directory in used_directory:
		for directory_path, directory_name, file_names in os.walk(directory):
			for file_name in file_names:
				os.system("dos2unix "+ directory_path + "/" + file_name )