#!/usr/bin/python

from itertools import *
from sys import maxint

usedList = {}

def getMatrix(fileName):
	allRows = list()
	theData = open(fileName)
	numElements = int(theData.readline())

	for _ in range(0,numElements):
		allRows.append([int(x) for x in theData.readline().split()])
	
	return allRows

def getDistMatrix(num):
	allDists = list() 
	for i in range(0,num):
		thisDist = list()
		for j in range(-i,num-i):
			thisDist.append(abs(j))
		allDists.append(thisDist)
	return allDists

def solve(matrix): 
	orders = permutations(range(1,len(matrix)+1))
	shortestDistance = maxint
	distMatrix = getDistMatrix(len(matrix))
	correctOrder = list()
	for order in orders:
		dist = getDist(order, matrix, distMatrix)
		if(dist < shortestDistance):
			correctOrder = order
			shortestDistance = dist
	return [correctOrder, shortestDistance]

def getDist(order, matrix, distMatrix):
	global usedList
	dist = 0
	for i in range(0,len(order)):
		whatsLeft = ''.join(str(x) for x in order[i:])
		if (whatsLeft in usedList):
			print "Was Dynamic"
			dist += usedList[whatsLeft]
			break
		else:
			print "Wasn't Dynamic"
			thisDist = 0
			for j in range(i,len(distMatrix[i])):
				thisDist += matrix[order[i]-1][order[j]-1] * distMatrix[i][j]
			usedList[whatsLeft] = thisDist
			dist += thisDist
	return dist	
