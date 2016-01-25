#!/usr/bin/env python3
#-*-coding:utf-8-*-
__author__ = 'IOT'
import socket
import re
def getip (url):
    try:
        ip = socket.gethostbyname(url)
        part = re.findall(r'.*\.',ip,re.S)
        Section = part+'0/24'
        ok = open('ok.txt','a+')
        IP = open('IP.txt','a+')
        Se = open('IP_Section.txt','a+')
        ok.writelines(ip + '\n')
        IP.writelines(line+' '+ip+'\n')
        Se.writelines(Section + '\n')
        print (line + ' >> '+ ip)
        print (ip + ' >> '+ Section)
    except:
        wrong = open ('fail.txt','a+')
        wrong.writelines(url + '\n')
        print (url + " can't be resolved")
site = open('url.txt','r')
for line in site:
    line = line.strip('\n')
    url = line.strip('https://')
    ip = getip(url)
