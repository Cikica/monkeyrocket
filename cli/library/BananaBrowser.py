#!/usr/bin/env python
import json

def get_value_from_a_json_file (file):
	data  = parse_and_return_json_file( file["path"] )
	try:
		value = data[file["value"]]
	except Exception:
		raise NameError("The key '"+ file["value"] +"' does not exist")
	else:
		return value

def parse_and_return_json_file( file_path ):

	file    = open(file_path, "r")
	content = file.read()
	value   = False
	file.close()
	try:
		value = json.loads(content)
	except ValueError:
		raise NameError("The "+ file_path +"file is not proper json, you probably added a comma where it does not belong, or missed a quote, check it.")
	else : 
		return value