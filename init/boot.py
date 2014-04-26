#!/usr/bin/env python

import os

directory = "/vagrant/init"
this_file_name = "boot.py"

for directory_path, directory_name, file_names in os.walk(directory):
	for file_name in file_names:
		if file_name != this_file_name:
			with open(directory_path + "/" + file_name, "r") as file_content:
				os.system(file_content.read())