#!/usr/bin/env python

class CommandHelp:

	def __init__(self, what):
		self.command        = what["command"]
		self.map            = what["map"]
		self.levels         = self.get_command_levels( what["map_order"] )
		self.full           = what["full"]
		self.is_full        = len( what["command"] ) == what["full"]

	def get_command_levels(self, command_map):
		levels = []
		for command in command_map:
			levels.append(command)

		return levels[0:len( self.command )]

	def is_given ( self, command ):
		
		return True if command in self.levels else False

	def only_has (self, level):
		return ( len( self.levels ) == 1 and level in self.levels )

	def has (self, what):
		return what in self.command

	def get (self, what):
		return self.command[self.levels.index(what)] if what in self.levels else False

	def is_valid (self, level ):

		valid_commands = self.map[level]
		command_text   = self.get(level)

		if not command_text:
			return False

		if len( valid_commands ) == 0 or command_text in valid_commands:
			return True
		else :
			return False