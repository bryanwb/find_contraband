#!/bin/env python
import os
from optparse import OptionParser

def findFiles(path):
	types = ['torrent', 'mp3', 'aac', 'wmv', 'mp4', 'mkv', 
		'mpeg', 'mpg', 'mov']

	findcmd = "find  " + path + "  -name '*." + types.pop() +  "'"

	for type in types:
		findcmd = findcmd + " -o -name '*." + type +  "'"

	#print findcmd
	stdin,hostname,stderr = os.popen3('hostname')
	stdin,stdout,stderr = os.popen3(findcmd)

	print hostname.readlines()[0]

	for line in stdout.readlines():
		print line

usage = "usage: %prog [path]"
parser = OptionParser(usage)
(options, args) = parser.parse_args()

path = "/" 
if (len(args) > 0):
	path = args[0]

findFiles(path)
