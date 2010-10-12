#!/usr/bin/python

import sys, os
import re

RE_DATA_HEADER=re.compile("data (?P<hostname>\S+)\.unige\.ch.listzone")

line=sys.stdin.readline()
while line:
	#print repr(line), type(line)
	line=sys.stdin.readline()
	match=RE_DATA_HEADER.match(line)
	if not match:
		continue
	else:
		print line
		line=sys.stdin.readline()
		print line


