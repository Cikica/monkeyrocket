#!/usr/bin/env python
import os
import importlib
# import json
# import subprocess
# import re
# from command_parser import Monkey_Command_Parser
# from banana_launcher import Monkey_Banana_Launcher
# from file_handler import Monkey_File_Handler

class Monkey:

	def make(self, what):

		if os.path.isdir(os.getcwd() + "/command/"+ what['<command>'][0]):
			module = importlib.import_module("command."+ what['<command>'][0] +".main")
			module.make(what['<command>'][1:], self)
	

	def do(self, what):
		parser = Monkey_Command_Parser()
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
		

	def deactivate_banana(self, banana):
		
		package_path = "/vagrant/bananas/"+ banana['name']
		banana_file = open( package_path +"/banana.json", "r")
		banana = json.loads(banana_file.read())
		for path in banana['purge']:
			subprocess.call([ package_path +"/"+ path ])

		self.remove_banana_name_from_active_list_file(banana['name'])