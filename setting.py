#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import re
import os


#上传的爬虫目录路径
upload_spider_dir = "/root/test_spider/"
#下载爬虫的存取目录
#server_spider_dir = "the_test_spider/"
#爬虫目录名
spider_dir = "myspider"
#所要爬虫的名字
run_spider_name = "readcolor"
#master服务器的地址、账号、密码
ip = "121.42.187.152"
user = "root"
password = "199411245015.wyp"

#slave服务器的地址、账号、密码
server_info = [
	["118.89.240.187", "ubuntu", "199411245015.wyp", "the_test_spider/"]
]
