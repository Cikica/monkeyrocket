#!/usr/bin/env python

from library import Command

class Monkey:

	def make(self, what):
		Command.run(what['<command>'])