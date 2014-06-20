#!/usr/bin/env python

def make(what):

	return [
		{
			"type"   : "shell",
			"source" : "install",
			"with"   : [
				what['configuration']['type']
			]
		}
	]