#!/usr/bin/env python

import subprocess

def make(command, monkey):

	valid_commands = ["launch", "purge"]
	valid_command = command[0] in valid_commands
	full_command = len(command) > 1

	if valid_command and full_command:

		if command[0] == "launch":
			launch(command[1:], monkey)

		if command[0] == "purge":
			print "purge"

	if not valid_command and full_command:
		print "Command \""+ command[0] +"\" is not a valid command for monkey rocket."

	if valid_command and not full_command:
		print "Command \""+ command[0] +"\" requires a package name as a argument."

def launch(command, monkey):
	banana = monkey.read_json_file_parse_it_and_return_its_value( monkey.banana_directory +"/"+ command[0] +"/banana.json" )
	for instruction in banana["launch"]:
		process_banana_instruction(instruction, command[0], monkey)

def process_banana_instruction(instruction, banana_name, monkey):

	if instruction['type'] == "shell":
		subprocess.call([ monkey.banana_directory +"/"+ banana_name +"/"+ instruction['source']+".sh"])

	if instruction['type'] == "command":
		monkey.run_command(instruction['source'])

def help():
	return "help stuff"

def purge(command):
	print command