#-*- coding:utf8 -*-
#就搜哦
import re
import requests
from datetime import datetime
# old_body_str = '''<http://img51.imgspice.com/i/03254/bzlgkt3zgfm1.jpeg'''
# small_img_re_str = r'(?P<img_url>(?P<img>http://img[\d]{0,3}.imgspice.com/i/[0-9]*/)(?P<img_name>.*?(?P<img_ext>.jpe?g)))'
#
# small_img_re = re.compile(small_img_re_str)
# small_imgs = re.finditer(small_img_re, old_body_str)
# small_imgs_dict = [ m.groupdict() for m in small_imgs]
# print small_imgs_dict
# url = 'http://img51.imgspice.com/i/03254/4zufduw65iav.jpeg'
# try:
# 	r = requests.get(url, timeout=0.01)
# 	print r
# except requests.exceptions.Timeout as e:
# 	print e
# big_img = 'http://img51.imgspice.com/i/03254/bzlgkt3zgfm1.jpeg'
# big_img_re_str = r'jpeg$'
# big_img_re =re.compile(big_img_re_str)
# big_img = re.sub(big_img_re,'jpg',big_img)
# print big_img

# n1 = 1
# n2 = 11
# r = float(1.0/11)
# print r

today = datetime.today()
print type(today)
# print type(today.date())
print today.day
start = datetime(today.year,today.month,today.day,23,59,59)
print start