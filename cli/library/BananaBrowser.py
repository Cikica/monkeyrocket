#!/usr/bin/env python
import json

def change_a_value_in_a_json_file(change):
	file    = open(change["file"], "r+")
	content = file.read()
	data    = parse_json_string({
		"content" : content,
		"file"    : change["file"]
	})
	print change
	data[change["key"]] = change["value"]
	file.seek(0)
	file.write(json.dumps( data ))
	file.truncate()
	file.close()

def get_the_value_of_a_key (get):
	try:
		value = get["hash"][get["key"]]
	except Exception:
		raise NameError("The key '"+ get["key"] +"' does not exist")
	else:
		return value

def get_value_from_a_json_file (get):
	data  = parse_and_return_json_file( get["file"] )
	try:
		value = data[get["key"]]
	except Exception:
		raise NameError("The key '"+ get["key"] +"' does not exist")
	else:
		return value

def parse_json_string (parse):
	try:
		value = json.loads(parse["content"])
	except ValueError:
		raise NameError("The "+ parse["file"] +"file is not proper json, you probably added a comma where it does not belong, or missed a quote, check it.")
	else : 
		return value

def parse_and_return_json_file( file_path ):

	file    = open(file_path, "r")
	content = file.read()
	value   = False
	file.close()
	return parse_json_string({
		"content" : content,
		"file"    : file_path
	})