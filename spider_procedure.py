#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import re
import os
from setting import *

def init():
#l = len(server_info)
	for var in server_info:
		command = '''expect scp_file.sh %s %s %s %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], ip, user, password, upload_spider_dir+spider_dir, var[3])
		os.system(command)

def run_spider():
	for var in server_info:
		run_command = '"nohup scrapy crawl ' + run_spider_name + ' &"'
		command = '''expect execute_command.sh %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], var[3] + spider_dir, run_command)
		os.system(command)

def kill_spider():
	for var in server_info:
		kill_command = '"killall scrapy"'
		command = '''expect execute_command.sh %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], var[3] + spider_dir, kill_command)
		os.system(command)

if __name__ == '__main__':

	while True:
		command = raw_input()
		if command == "exit":
			break
		if command == "init":
			init()
		if command == "run":
			run_spider()
		if command == "kill":
			kill_spider()

