#!/usr/bin/env python

import importlib
import subprocess
import json
import os
from library.CommandHelp import CommandHelp
from library import BananaBrowser
from library import Command

def make(passed_command, directory):
	command = CommandHelp({
		"command"   : passed_command,
		"full"      : 2,
		"map_order" : ["action", "name", "configuration"],
		"map"       : {
			"action"        : ["launch", "purge", "help"],
			"name"          : [],
			"configuration" : []
		}
	})
	
	if command.only_has("action") and command.has("help"):
		help()

	elif not command.is_valid("action"):
		print "Command \""+ command.get("action") +"\" is not a valid command for monkey rocket."

	elif command.is_valid("action") and not command.is_given("name") and not command.has("help"):
		print "Command \""+ command.get("action") +"\" requires a package name as a argument."

	else: 
		banana = diagonse_banana({
			"command"   : command,
			"directory" : directory
		})

		if not banana["can_launch"]:
			report_diagnosis(banana)

		if banana["can_launch"] and command.has("launch"):
			launch({
				"banana" : command.get("name"),
				"with"   : get_banana_launch_instruction({
					"of"   : command.get("name"),
					"with" : command.get("configuration"),
					"path" : directory["banana"] +"/"+ command.get("name") +"/banana.json",
					"pass" : directory
				})
			})
			
			BananaBrowser.change_a_value_in_a_json_file({
				"file"  : directory["banana_file"],
				"key"   : "active",
				"value" : BananaBrowser.get_value_from_a_json_file({
					"file"  : directory["banana_file"],
					"key"   : "active"
				}) + [command.get("name")]
			})


def report_diagnosis (banana):

	if banana["active"]:
		print "Banana is already active"

	if not banana["exists"]:
		print "Banana does not exist"

	if banana["exists"] and not banana["has_json"]:
		print "The banana does not have a banana.json defintion thus it can not work"

def get_banana_launch_instruction (instruction):

	banana_file              = BananaBrowser.parse_and_return_json_file( instruction["path"] )
	comes_with_configuration = instruction["with"] != False
	requires_configuration   = banana_file.has_key("configuration")
	has_launch_list          = banana_file.has_key("launch")

	if requires_configuration:
		banana_module  = importlib.import_module("banana."+ instruction["of"] +".banana")
		return banana_module.make({
			"banana_directory" : instruction["pass"],
			"configuration"    : instruction["with"] if comes_with_configuration else process_banana_configuration(banana_file["configuration"] )
		})
	elif has_launch_list:
		return banana_file["launch"]
	else:
		return False



def diagonse_banana (monkey):
	banana_directory     = monkey["directory"]["banana"] +"/"+ monkey["command"].get("name")
	banana_is_present    = os.path.isdir( banana_directory )
	banana_json_is_here  = os.path.exists( banana_directory +"/banana.json" )
	active_bananas       = BananaBrowser.get_value_from_a_json_file({ 
		"file" : monkey["directory"]["banana_file"],
		"key"  : "active"
	})
	banana_is_not_active = monkey["command"].get("name") not in active_bananas
	return {
		"exists"     : banana_is_present,
		"has_json"   : banana_json_is_here,
		"active"     : not banana_is_not_active,
		"can_launch" : ( banana_is_not_active and banana_is_present and banana_json_is_here )
	}

def launch(what):

	for instruction in what["with"]:

		if instruction['type'] == "shell":
			this_banana_directory = monkey.banana_directory +"/"+ banana_name
			shell_arguments       = [ monkey.directory, this_banana_directory ] + instruction['with']
			subprocess.call([ this_banana_directory +"/"+ instruction['source'] +".sh" ] + shell_arguments )

		if instruction['type'] == "command":
			Command.run(instruction['source'])

def process_banana_configuration(configuration):

	definition = {}
	for option in configuration:
		definition[option] = process_a_configuration_option(configuration[option])

	return definition

def process_a_configuration_option(option):

	value = raw_input(option['text'])
	return option['default'] if not value else value

def help():
	text = "\nrocket\n  commands:\n"
	text = text +"    launch <package_name> <configuration>?\n"
	text = text +"      Launch a package. Package will not be launched if it is found to be already active.\n"
	print text