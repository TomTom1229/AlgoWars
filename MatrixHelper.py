#!/usr/bin/python

from itertools import *
from sys import maxint
import random

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
	distMatrix = getDistMatrix(len(matrix))
	if(len(matrix) > 10):
		orders = getSubsetOfAllPermutations(len(matrix))
	else:
		orders = list(permutations(range(1,len(matrix)+1)))
		#orders = breakAbsoluteSolution(orders, matrix)
	shortestDistance = maxint
	correctOrder = list()
	for order in orders:
		dist = getDist(order[::-1], matrix, distMatrix) # taking advantage of lexigraphic ordering
		if(dist < shortestDistance):
			correctOrder = order[::-1]
			shortestDistance = dist
	return [correctOrder, shortestDistance]

def getDist(order, matrix, distMatrix):
	global usedList
	dist = 0
	for i in range(0,len(order)):
			thisDist = 0
			for j in range(i,len(distMatrix[i])):
				thisDist += matrix[order[i]-1][order[j]-1] * distMatrix[i][j]
			dist += thisDist
	return dist	

def printMatrix(order, matrix):
	newMatrix = reorderMatrix(order, matrix)
	for down in newMatrix:
		for over in down:
			print str(over),
		print
	print

def reorderMatrix(order, matrix):
	newMatrix = list()
	for down in order:
		row = list()
		for over in order:
			row.append(str(matrix[down-1][over-1]))
		newMatrix.append(row)
	return newMatrix

def getSubsetOfAllPermutations(num):
	subset = list()
	theElements = range(1,num+1)
	numToSubset = 40320 #8!
	while numToSubset:
		random.shuffle(theElements)
		if (theElements not in subset and theElements[::-1] not in subset):
			subset.append(list(theElements))
			numToSubset -= 1
	return subset

def check(orderLine, matrix):
	order = [int(x) for x in orderLine.split()]
	return getDist(order, matrix, getDistMatrix(len(matrix)))
