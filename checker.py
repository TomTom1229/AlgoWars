#!/usr/bin/python

from sys import argv
from MatrixHelper import *

if len(argv) != 3: 
	print "Must give test file and output file"
	exit(-1)

connectiveMatrix = getMatrix(argv[1])

isFirst = True
correct = 0
for line in open(argv[2]):
	if(isFirst):
		correct = check(line, connectiveMatrix)
		isFirst = False
	else:
		theirs = int(line)

if(theirs == correct):
	print "Valid"
else:
	print "Invalid"
