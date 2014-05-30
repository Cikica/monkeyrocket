#!/usr/bin/env python
import importlib
import subprocess
import json

def make(command, monkey):

	valid_commands = ["launch", "purge"]
	valid_command = command[0] in valid_commands
	full_command = len(command) > 1
	has_configuration = True if len(command) > 2 else False

	if valid_command and full_command:

		if command[0] == "launch":
			launch({
				"line"              : command[1:],
				"has_configuration" : has_configuration,
				"monkey"            : monkey
			})

		if command[0] == "purge":
			print "purge"

	if not valid_command and full_command:
		print "Command \""+ command[0] +"\" is not a valid command for monkey rocket."

	if valid_command and not full_command:
		print "Command \""+ command[0] +"\" requires a package name as a argument."

def launch(command):
	
	banana = command['monkey'].read_json_file_parse_it_and_return_its_value( command['monkey'].banana_directory +"/"+ command['line'][0] +"/banana.json" )

	if banana.has_key("configuration"):
		banana_module = importlib.import_module("banana."+ command['line'][0] +".banana")
		configuration = json.loads(command['line'][1]) if command['has_configuration'] else process_banana_configuration(banana['configuration'])
		launch_list = banana_module.make({
			"banana_directory" : command['monkey'].banana_directory +"/"+ command['line'][0],
			"configuration"    : configuration
		})
	else:
		launch_list = banana['launch']

	for instruction in launch_list:
		process_banana_instruction(instruction, command['line'][0], command['monkey'])

def process_banana_instruction(instruction, banana_name, monkey):

	if instruction['type'] == "shell":
		this_banana_directory = monkey.banana_directory +"/"+ banana_name
		shell_arguments = [ monkey.directory,this_banana_directory ] + instruction['with']
		subprocess.call([ 
			this_banana_directory +"/"+ instruction['source']+".sh"
		] + shell_arguments )

	if instruction['type'] == "command":
		monkey.run_command(instruction['source'])

def process_banana_configuration(configuration):

	definition = {}
	for option in configuration:
		definition[option] = process_a_configuration_option(configuration[option])
	return definition

def process_a_configuration_option(option):
	value = raw_input(option['text'])
	return option['default'] if not value else value


def help():
	return "help stuff"

def purge(command):
	print command