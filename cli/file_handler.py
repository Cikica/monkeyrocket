#!/usr/bin/env python

import json
import os

def read_json_file_parse_it_and_return_its_value(file_path):
	file = open(file_path, "r")
	value = json.loads(file.read())
	file.close()
	return value

def get_known_packages(self):
	return read_json_file_parse_it_and_return_its_value("/vagrant/bananas/known_packages.json")

def get_active_packages(self):
	return read_json_file_parse_it_and_return_its_value("/vagrant/bananas/active_packages.json")

def remove_banana_name_from_active_list_file(package_name):
	active_packages = get_active_packages()
	file = open("/vagrant/bananas/active_packages.json", "w+")
	active_packages.pop(active_packages.index(package_name))
	file.write(json.dumps(active_packages))
	file.close()

def add_banana_name_to_active_list_file(package_name):
	active_packages = get_active_packages()
	file = open("/vagrant/bananas/active_packages.json", "w+")
	if package_name not in active_packages:
		active_packages.append(package_name)
		file.write(json.dumps(active_packages))
	file.close()

def make_banana_definition(command):
	
	bananas = {
		"known"  : get_known_packages(),
		"active" : get_active_packages()
	}

	return {
		"name"         : command['<banana_name>'],
		"is_active"    : command['<banana_name>'] in bananas['active'],
		"is_installed" : os.path.exists("/vagrant/bananas/"+ command['<banana_name>'] ),
		"is_known"     : bananas['known'].has_key(command['<banana_name>']),
		"url"          : resolve_banana_url({
			"name" : command['<banana_name>'],
			"url"  : command['<banana_url>']
		})
	}

def resolve_banana_url(banana):

	known_bananas = get_known_packages()

	if banana['url'] != None:
		return banana['url']
	if known_bananas.has_key(banana['name']):
		return known_bananas[banana['name']]

	return None