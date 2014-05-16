#!/usr/bin/env python
import os
import json
import subprocess
import re

class Monkey:

	def do(self, what):
		# self.handle_the_action_definition(
		print self.parse_command_and_return_definition(what)

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

	def read_json_file_parse_it_and_return_its_value(self, file_path):
		file = open(file_path, "r")
		value = json.loads(file.read())
		file.close()
		return value

	def get_known_packages(self):
		return self.read_json_file_parse_it_and_return_its_value("/vagrant/bananas/known_packages.json")

	def get_active_packages(self):
		return self.read_json_file_parse_it_and_return_its_value("/vagrant/bananas/active_packages.json")

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

	def parse_command_and_return_definition(self, command):

		banana_information = self.get_banana_information(command['<banana_name>'])

		if command['banana']:
			return self.make_definition_out_of_banana_command(command, banana_information)
			
		if command['rocket']:
			return self.make_definition_out_of_rocket_command(command, banana_information)
			
	def make_definition_out_of_rocket_command(self, command, banana):

		if command['add']:
			action = self.resolve_add_command_action(command, banana, "rocket" )
			definition = self.make_action_definition({
				"name" : command['<banana_name>'],
				"url"  : self.resolve_banana_url({
					"name"     : command['<banana_name>'],
					"url"      : command['<banana_url>'],
					"is_known" : banana['is_known'],
				})
			})
			return definition['rocket'][action]

		if command['remove']:
			if banana['is_active']:
				return "deactivate"
			return "nothing"


	def make_definition_out_of_banana_command(self, command, banana):

		if command['add']:
			return self.resolve_add_command_action(command, banana, "banana")

		if command['remove']:
			if banana['is_installed']:
				return "delete"
			return "nothing"

	def resolve_add_command_action(self, command, banana, type):
		if banana['is_active'] and banana['is_installed']:
			return "nothing"

		if banana['is_active'] == False and banana['is_installed']:
			return "nothing" if type == "banana" else "launch"

		if banana['is_installed'] == False and banana['is_known']:
			return "download" if type == "banana" else "download:launch"

		if command['<banana_url>'] != None:
			return "download" if type == "banana" else "download:launch"

		return "error"

	def resolve_banana_url(self, banana):

		known_bananas = self.get_known_packages()

		if banana['url'] != None:
			return banana['url']
		if banana['is_known']:
			return known_bananas[banana['name']]

		return None


	def get_banana_information(self, banana_name):
		
		bananas = {
			"known"  : self.get_known_packages(),
			"active" : self.get_active_packages()
		}

		return {
			"is_active"    : banana_name in bananas['active'],
			"is_installed" : os.path.exists("/vagrant/bananas/"+ banana_name ),
			"is_known"     : bananas['known'].has_key(banana_name)
		}

	def make_action_definition(self, banana):
		return {
			"rocket" : {
				"nothing" : {
					"report" : {
						"text" : "Banana is already active"
					}
				},
				"launch" : {
					"launch_banana" : {
						"banana_name" : banana['name']
					},
					"report" : {
						"text" : "Banana launched"
					}
				},
				"download:launch" : {
					"prompt" : {
						"text"       : "Banana needs to be downloaded first before it can be launched, procceed?(y/n)",
						"is_true_if" : ["y", "yes", "Y", "Yes", "YES"],
						"if_true"    : {
							"download_banana" : {
								"banana_name" : banana['name'],
								"banana_url"  : banana['url'],
								"when_done"   : {
									"launch_banana" : {
										"banana_name" : banana['name']
									},
									"report" : {
										"text" : "Banana is launched"
									}
								}
							}

						}
					}
				},
				"deactivate" : {
					"deactivate_banana" : {
						"banana_name" : banana['name']
					}
				},
				"error" : {
					"report" : {
						"text" : "The banana name is not known or downloaded, and a valid banana url has not been provided so that it may be added."
					}
				}
			},
			"banana" : {},
		}
