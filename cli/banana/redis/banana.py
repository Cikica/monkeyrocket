#!/usr/bin/env python

import fileinput
import os
from shutil import copyfile

def make(what):
	
	init_file_path = what['banana_directory'] +"/conf/redis_"+ what['configuration']['port']
	conf_file_path = what['banana_directory'] +"/conf/"+ what['configuration']['port'] +".conf"

	copyfile( what['banana_directory'] +"/conf/redis_init_template", init_file_path)
	copyfile( what['banana_directory'] +"/conf/redis.conf", conf_file_path)

	for line in fileinput.input(init_file_path, inplace=True):
		if fileinput.filelineno() == 6:
			print "%s" % "REDISPORT="+ what['configuration']['port']
		else:
			print "%s" % (line),

	for line in fileinput.input(conf_file_path, inplace=True):
		if fileinput.filelineno() == 41:
			print "%s" % "pidfile /var/run/redis_"+ what['configuration']['port'] +".pid"
		elif fileinput.filelineno() == 45:
			print "%s" % "port "+ what['configuration']['port']
		elif fileinput.filelineno() == 64:
			print "%s" % "bind "+ what['configuration']['bind']
		elif fileinput.filelineno() == 187:
			print "%s" % "dir /var/redis/"+ what['configuration']['bind']
		else:
			print "%s" % (line),

	return [
		{
			"type"   : "shell",
			"source" : "install/install",
			"with"   : [
				what['configuration']['port'],
				init_file_path,
				conf_file_path
			]
		}
	]