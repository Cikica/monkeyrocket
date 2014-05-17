#!/usr/bin/env python

import json

class Monkey_Banana_Launcher:

	def make(self, banana):
		banana_definition = self.get_banana_file(banana['name'])
		print banana_definition

	def get_banana_file(self, banana_name):
		banana_file = open("/vagrant/bananas/"+ banana_name +"/banana.json")
		definition  = json.loads(banana_file.read())
		banana_file.close()
		return definition