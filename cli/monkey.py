#!/usr/bin/env python
import os
import importlib
import json

class Monkey:

	def get_directory_hash(self):
		cwd = os.getcwd()
		return {
			"main"        : cwd,
			"banana"      : cwd +"/banana",
			"banana_file" : cwd +"/banana/banana.json",
			"command"     : cwd +"/command"
		}

	def make(self, what):
		self.run_command(what['<command>'])

	def run_command(self, command):
		if os.path.isdir(os.getcwd() + "/command/"+ command[0]):
			module = importlib.import_module("command."+ command[0] +".main")
			module.make(command[1:], self.get_directory_hash())