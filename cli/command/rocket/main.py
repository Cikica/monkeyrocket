#!/usr/bin/env python

def make(command, monkey):

	valid_commands = ["launch", "purge"]
	valid_command = command[0] in valid_commands
	full_command = len(command) > 1

	if valid_command and full_command:
		if command[0] == "launch":
			launch(command[1:])
		if command[0] == "purge":
			print "purge"

	if not valid_command and full_command:
		print "Command \""+ command[0] +"\" is not a valid command for monkey rocket."

	if valid_command and not full_command:
		print "Command \""+ command[0] +"\" requires a package name as a argument."

def launch(command):
	print command

def purge(command):
	print command