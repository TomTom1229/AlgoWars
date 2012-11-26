#!/usr/bin/python

from itertools import *
from sys import maxint
import math 

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
	orders = permutations(range(1,len(matrix)+1)) #Because of inclusion and zero based indices
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
	dist = 0
	for i in range(0,len(order)):
		for j in range(i,len(distMatrix[i])):
			dist += matrix[order[i]-1][order[j]-1] * distMatrix[i][j]	
	return dist	
