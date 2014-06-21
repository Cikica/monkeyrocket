#!/usr/bin/env python

from distutils.core import setup

setup(
	name='monkey', 
	version='0.1',
	py_modules=[
		'monkey'
	],
	packages=[
		"library", 
		"command",
		"command.rocket",
		"banana",
		"banana.redis",
		"banana.nginx",
		"banana.php",
		"banana.laravel"
	],
	author='Aleksandar Andjelkovic', 
	author_email='aleksandar.andjelkovich@gmail.com',
	url='www.getsome.com',
)