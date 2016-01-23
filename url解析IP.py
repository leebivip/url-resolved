#!/usr/bin/env python3
#-*-coding:utf-8-*-
__author__ = 'IOT'
import socket
def getip (url):
    try:
        ip = socket.gethostbyname(url)
        ok = open('ok.txt','a+')
        IP = open('IP.txt','a+')
        ok.writelines(ip + '\n')
        IP.writelines(line+' '+ip+'\n')
        print (line + ' >> '+ ip)
    except:
        wrong = open ('fail.txt','a+')
        wrong.writelines(url + '\n')
        print (url + " can't be resolved")
site = open('url.txt','r')
for line in site:
    line = line.strip('\n')
    url = line.strip('https://')
    ip = getip(url)
