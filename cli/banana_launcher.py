#!/usr/bin/env python

import json
import subprocess
from banana_configure import Monkey_Banana_Configure

class Monkey_Banana_Launcher:

	def make(self, banana):

		banana_definition = self.get_banana_file(banana['name'])

		if banana_definition.has_key("configure"):
			self.setup_with_configuration(banana_definition, banana)

	def setup_with_configuration(self, banana_definition, banana):
		banana_configure = Monkey_Banana_Configure()
		definition = banana_configure.make(banana_definition['configure'])

		if banana_definition['pass_configuration']['to'] == "shell":
			subprocess.call(["/vagrant/bananas/"+ banana['name'] +"/"+ banana_definition['pass_configuration']['source'] +".sh"] + definition )

	def get_banana_file(self, banana_name):
		banana_file = open("/vagrant/bananas/"+ banana_name +"/banana.json")
		definition  = json.loads(banana_file.read())
		banana_file.close()
		return definition