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
		upload_path = user + '@' + ip + ':' + upload_spider_dir + spider_dir
		download_path = var[3]
#		command = '''expect scp_file.sh %s %s %s %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], ip, user, password, upload_spider_dir+spider_dir, var[3])
		command = '''expect scp_file.sh %s %s %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], upload_path, download_path, password, "2")
		os.system(command)

def run_spider():
	for var in server_info:
		run_command = '"nohup scrapy crawl ' + run_spider_name + ' &"'
		command = '''expect execute_command.sh %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], var[3] + spider_dir, run_command)
		os.system(command)

def kill_spider():
	for var in server_info:
		kill_command = '"killall -9 scrapy"'
		command = '''expect execute_command.sh %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], var[3] + spider_dir, kill_command)
		os.system(command)

def collect_page():
	for var in server_info:
		upload_path = var[3] + spider_dir + '/' + server_page_path + "*"
		download_path = user + '@' + ip + ':' + client_page_path 
		command = '''expect scp_file.sh %s %s %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], upload_path, download_path, password, "1")
		os.system(command)

def clear_page():
	for var in server_info:
		rm_command = '"rm ' + server_page_path + '*"'
		command = '''expect execute_command.sh %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], var[3] + spider_dir, rm_command)
		os.system(command)

def delete_spider():
	for var in server_info:
		rm_command = '"rm -r ' + var[3] + '"'
		command = '''expect execute_command.sh %s %s %s %s %s 2>>log'''%(var[0], var[1], var[2], ".", rm_command)
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
		if command == "collect":
			collect_page()
		if command == "clear":
			clear_page()
		if command == "delete":
			delete_spider()

