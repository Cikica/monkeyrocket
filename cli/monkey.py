#!/usr/bin/env python
import os
import importlib
import json

class Monkey:

	def __init__(self):
		self.directory = os.getcwd()
		self.banana_directory = self.directory +"/banana"

	def make(self, what):
		self.run_command(what['<command>'])

	def run_command(self, command):
		if os.path.isdir(os.getcwd() + "/command/"+ command[0]):
			module = importlib.import_module("command."+ command[0] +".main")
			module.make(command[1:], self)

	def read_json_file_parse_it_and_return_its_value(self, file_path):
		file = open(file_path, "r")
		content = file.read()
		file.close()
		value = False
		try:
			value = json.loads(content)
		except ValueError:
			raise NameError("The "+ file_path +"file is not proper json, you probably added a comma where it does not belong, or missed a quote, check it.")
		else : 
			return value