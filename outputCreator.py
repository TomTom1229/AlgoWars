#!/usr/bin/python

from sys import argv
from random import randint


numElements = int(argv[1])

testFile = open("test"+str(numElements),'w')

testFile.write(str(numElements)+"\n")
upperHalf = list()
for i in range(0,numElements):
	row = list()
	for j in range(i+1,numElements):
		row.append(str(randint(0,100)))
	upperHalf.append(row)

for i in range(0, numElements):
	upperHalf[i].insert(0,"0")
	for j in range(0,i):
		upperHalf[i].insert(j ,upperHalf[j][i])

testFile.write('\n'.join(' '.join(x) for x in upperHalf))
