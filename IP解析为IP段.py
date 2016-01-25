#!/usr/bin/env python3
#-*-coding:utf-8-*-
__author__ = 'IOT'
import re
IP =("1.2.3.4")
h = re.findall("..",IP,re.S)
S = h[0]+h[1]+h[2]+'0/24'
print (S)
