#!/usr/bin/env python

class Monkey_Banana_Configure:

	def make(self, what):
		configuration = []
		for option in what:
			configuration.append(raw_input("\n"+ option['text'] +"\n"))

		return configuration