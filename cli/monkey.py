#!/usr/bin/env python
import os
import json
import subprocess

class Monkey:

	def do(self, what):
		self.handle_the_action_definition(self.parse_the_instructions_and_return_action_definition(what))

	def handle_the_action_definition(self, definition):
		getattr(self, definition['action'])(definition['give'])

	def report(self, what):
		print what

	def prompt(self, do):
		response = raw_input(do['say'])
		go_or_no_go = "if_go" if response in do['proceed'] else "if_no_go"
		getattr(self, do[go_or_no_go]['action'] )( do[go_or_no_go]['give'] )

	def add_package(self, package):
		print package

	def get_known_and_active_packages_list (self):
		known_packages_file = open("/vagrant/bananas/known_packages.json", "r")
		active_packages_file = open("/vagrant/bananas/active_packages.json", "r")
		packages = { 
			"known" : json.loads(known_packages_file.read()),
			"active" : json.loads(active_packages_file.read())
		}
		known_packages_file.close()
		active_packages_file.close()
		return packages

	def setup_package(self, package):
		package_path = "/vagrant/bananas/"+ package['name']
		banana_file = open( package_path +"/banana.json", "r")
		banana = json.loads(banana_file.read())
		for path in banana['setup']:
			subprocess.call([ package_path +"/"+ path ])

		self.add_package_name_to_active_packages(package['name'])

	def purge_package(self, package):
		package_path = "/vagrant/bananas/"+ package['name']
		banana_file = open( package_path +"/banana.json", "r")
		banana = json.loads(banana_file.read())
		for path in banana['purge']:
			subprocess.call([ package_path +"/"+ path ])
		self.remove_package_name_from_active_packages(package['name'])


	def get_active_packages(self):
		file = open("/vagrant/bananas/active_packages.json", "r")
		active_packages = json.loads(file.read())
		file.close()
		return active_packages

	def remove_package_name_from_active_packages(self, package_name):
		active_packages = self.get_active_packages()
		file = open("/vagrant/bananas/active_packages.json", "w+")
		active_packages.pop(active_packages.index(package_name))
		file.write(json.dumps(active_packages))
		file.close()

	def add_package_name_to_active_packages(self, package_name):
		active_packages = self.get_active_packages()
		file = open("/vagrant/bananas/active_packages.json", "w+")
		if package_name not in active_packages:
			active_packages.append(package_name)
			file.write(json.dumps(active_packages))
		file.close()

	def parse_the_instructions_and_return_action_definition(self, do):

		packages = self.get_known_and_active_packages_list()
		is_package_installed = os.path.exists("/vagrant/bananas/"+ do['<package_name>'] )
		is_known_package = packages['known'].has_key(do['<package_name>'])
		is_active_package = do['<package_name>'] in packages['active']
		definition = {
			"action" : "",
			"give"   : ""
		}

		if do['add'] == True and is_package_installed == True:
			return { 
				"action" : "report",
				"give" : "The package "+ do['<package_name>'] +" is already a banana and can be setup."
			}

		if do['add'] == True and is_package_installed == False and is_known_package == True:
			return {
				"action" : "prompt",
				"give" : {
					"say"     : "The package "+ do['<package_name>'] +" is not a banana; but is know know to me. Shall i get it? (Yes/No)",
					"proceed" : ["yes", "Y", "Yes", "y"],
					"if_go"   : {
						"action" : "add_package", 
						"give"   : {
							"url"    : packages['known'].get(do['<package_name>']),
							"name"   : do['<package_name>']
						}
					},
					"if_no_go": {
						"action" : "report",
						"give"   : "Oke aborting."
					}
				}
			}

		if do['setup'] == True and is_active_package == False and is_package_installed == False and is_known_package == False:
			print "package is not known"

		if do['setup'] == True and is_active_package == False and is_package_installed == False and is_known_package == True:
			print "package is know and can be installed"

		if do['setup'] == True and is_active_package == True:
			return {
				"action" : "report",
				"give"   : "The package "+ do['<package_name>'] +" happens to be already setup."
			}

		if do['setup'] == True and is_package_installed == True and is_active_package == False:
			return { 
				"action" : "setup_package",
				"give"   : {
					"name" : do['<package_name>']
				}
			}

		if do['purge'] == True and is_active_package == True:
			return {
				"action" : "purge_package",
				"give"   : { 
					"name" : do['<package_name>']	
				}
			}

		if do['purge'] == True and is_active_package == False:
			return { 
				"action" : "report",
				"give"   : "There is no record of this package being active, thus it can not be purged."
			}
