#!/usr/bin/env python
# big dreams for this bad boy
# at some point this module can be turned into a module that allows us to register every command and sub command of 
# that command and so on as a self conainted module, and keep the chaining logic of those commands in this
# file right here, and handle the optiosns wiht some more magic ( dosent make sense? wait will you see)
# for not just some humble code

import os
import importlib

def run(command):
	if os.path.isdir(os.getcwd() + "/command/"+ command[0]):
		module = importlib.import_module("command."+ command[0] +".main")
		module.make(command[1:], get_directory_hash())

def get_directory_hash():
	cwd = os.getcwd()
	return {
		"main"        : cwd,
		"banana"      : cwd +"/banana",
		"banana_file" : cwd +"/banana/banana.json",
		"command"     : cwd +"/command"
	}