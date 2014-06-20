#!/usr/bin/env python

import unittest
from library.CommandHelp import CommandHelp

class TestCommandHelp(unittest.TestCase):

	def setUp(self):
		self.paramaters = {
			"command"   : ["launch"],
			"full"      : 2,
			"map_order" : ["action", "name", "configuration"],
			"map"       : {
				"action"        : ["launch", "purge", "help"],
				"configuration" : []
			}
		}
		self.command_help = CommandHelp(self.paramaters)

	def test_if_basic_initiation_is_correct(self):

		self.assertEqual( self.command_help.command, self.paramaters["command"] )
		self.assertEqual( self.command_help.map, self.paramaters["map"] )
		self.assertEqual( self.command_help.full, self.paramaters["full"] )
		self.assertEqual( self.command_help.levels, ["action"] )
		self.assertEqual( self.command_help.is_full, False )

	def test_is_given(self):
		self.assertTrue( self.command_help.is_given( "action" ) )
		self.assertFalse( self.command_help.is_given( "configuration" ) )

	def test_only_has(self):
		self.assertTrue( self.command_help.only_has( "action" ) )

	def test_has(self):
		self.assertTrue( self.command_help.has( "launch" ) )
		self.assertFalse( self.command_help.has( "some" ) )

	def test_get(self):
		self.assertEquals( "launch", self.command_help.get( "action" ) )
		self.assertEquals( False, self.command_help.get( "configuration" ) )

	def test_is_valid(self):
		self.assertTrue( self.command_help.is_valid("action") )
		self.assertFalse( self.command_help.is_valid("configuration") )