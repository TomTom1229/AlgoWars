#!/usr/bin/python

from sys import argv
from random import randint


numElements = int(argv[1])

testFile = open("test"+str(numElements),'w')

testFile.write(str(numElements)+"\n")
for i in range(0,numElements):
	for j in range(0,numElements):
		testFile.write(str(randint(0,5))+" ")
	testFile.write("\n")

