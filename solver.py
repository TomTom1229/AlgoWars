#!/usr/bin/python

from MatrixHelper import *
from sys import argv 

if len(argv) != 2: 
	print "Must give file"
	exit(-1)

connectiveMatrix = getMatrix(argv[1])
order, cost = solve(connectiveMatrix)

for i in order:
	print i,
print
print cost
