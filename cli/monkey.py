#!/usr/bin/env python
import os
import json
import subprocess
import re
import command_parser

class Monkey:

	def do(self, what):
		parser = command_parser.Monkey_Command_Parser()
		self.act_based_on_definition(parser.make(what, self.make_banana_definition(what)))

	def act_based_on_definition(self, definition):

		for action in definition:
			self.call_a_method_of_the_class_and_pass_instructions({
				"name"         : action,
				"instructions" : definition[action]
			})

	def call_a_method_of_the_class_and_pass_instructions(self, method):
		getattr(self, method['name'])(method['instructions'])

	def report(self, what):
		print "\n"+ what['text'] +"\n"

	def prompt(self, do):
		response = raw_input("\n"+ do['text'] +"\n")
		true_or_false = "if_true" if response in do['is_true_if'] else "if_false"
		self.act_based_on_definition(do[true_or_false])

	def launch_banana(self, banana):

		package_path = "/vagrant/bananas/"+ banana['name']
		banana_file = open( package_path +"/banana.json", "r")
		banana = json.loads(banana_file.read())
		for path in banana['setup']:
			subprocess.call([ package_path +"/"+ path ])

		self.add_banana_name_to_active_list_file(banana['name'])
		

	def deactivate_banana(self, banana):
		
		package_path = "/vagrant/bananas/"+ banana['name']
		banana_file = open( package_path +"/banana.json", "r")
		banana = json.loads(banana_file.read())
		for path in banana['purge']:
			subprocess.call([ package_path +"/"+ path ])

		self.remove_banana_name_from_active_list_file(banana['name'])

	def read_json_file_parse_it_and_return_its_value(self, file_path):
		file = open(file_path, "r")
		value = json.loads(file.read())
		file.close()
		return value

	def get_known_packages(self):
		return self.read_json_file_parse_it_and_return_its_value("/vagrant/bananas/known_packages.json")

	def get_active_packages(self):
		return self.read_json_file_parse_it_and_return_its_value("/vagrant/bananas/active_packages.json")

	def remove_banana_name_from_active_list_file(self, package_name):
		active_packages = self.get_active_packages()
		file = open("/vagrant/bananas/active_packages.json", "w+")
		active_packages.pop(active_packages.index(package_name))
		file.write(json.dumps(active_packages))
		file.close()

	def add_banana_name_to_active_list_file(self, package_name):
		active_packages = self.get_active_packages()
		file = open("/vagrant/bananas/active_packages.json", "w+")
		if package_name not in active_packages:
			active_packages.append(package_name)
			file.write(json.dumps(active_packages))
		file.close()

	def make_banana_definition(self, command):
		
		bananas = {
			"known"  : self.get_known_packages(),
			"active" : self.get_active_packages()
		}

		return {
			"name"         : command['<banana_name>'],
			"is_active"    : command['<banana_name>'] in bananas['active'],
			"is_installed" : os.path.exists("/vagrant/bananas/"+ command['<banana_name>'] ),
			"is_known"     : bananas['known'].has_key(command['<banana_name>']),
			"url"          : self.resolve_banana_url({
				"name" : command['<banana_name>'],
				"url"  : command['<banana_url>']
			})
		}

	def resolve_banana_url(self, banana):

		known_bananas = self.get_known_packages()

		if banana['url'] != None:
			return banana['url']
		if known_bananas.has_key(banana['name']):
			return known_bananas[banana['name']]

		return None