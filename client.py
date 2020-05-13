#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# PHP 危险函数整理，包含windows平台的
# https://stackoverflow.com/questions/3115559/exploitable-php-functions
# 

import sys
import os
import re
import json
import requests
import itertools

known_classes   = {}
known_functions = {}

def load_config():
	global known_functions, known_classes

	basedir = os.path.dirname(os.path.realpath(__file__))

	with open(basedir + '/config/functions.json', 'r') as f:
		known_functions = json.loads(f.read())

	with open(basedir + '/config/class.json', 'r') as f:
		known_classes   = json.loads(f.read())

def run(url):
	resp = requests.get(url)
	print '[-] Raw response:', "\n\n", resp.text

	data              = json.loads(resp.text)
	disable_functions = data['disable_functions']
	disable_classes   = data['disable_classes']

	print '[-] Parse result'

	for cat in known_functions:
		print "\n", '[function: %s]' % (cat)

		for name in known_functions[cat]:
			if name not in disable_functions:
				print name

	for cat in known_classes:
		print "\n", '[class: %s]' % (cat)

		for name in known_classes[cat]:
			if name not in disable_classes:
				print name
				

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage:', sys.argv[0], 'URL'
		sys.exit()

	load_config()
	run(sys.argv[1])





