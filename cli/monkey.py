#!/usr/bin/env python
import os
import json

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

	def install_package(self, package):
		print "instaling"


	def parse_the_instructions_and_return_action_definition(self, do):
		
		known_packages_file = open("/vagrant/bananas/known_packages.json", "r")
		known_packages = json.loads(known_packages_file.read())
		known_packages_file.close()
		is_package_installed = os.path.exists("/vagrant/bananas/"+ do['<package_name>'] )
		is_known_package = known_packages.has_key(do['<package_name>'])
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
						"action" : "install_package", 
						"give"   : {
							"url"    : known_packages.get(do['<package_name>']),
							"name"   : do['<package_name>']
						}
					},
					"if_no_go": {
						"action" : "report",
						"give"   : "Oke aborting."
					}
				}
			}