#!/usr/bin/python

from itertools import *
from sys import maxint
from multiprocessing import cpu_count
import threading

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
	orders = permutations(range(1,len(matrix)+1)) # All Possible
	distMatrix = getDistMatrix(len(matrix))
	if(len(matrix) > 8):
		orders = breakAbsoluteSolution(orders, matrix)
	print(len(orders))
	shortestDistance = maxint
	correctOrder = list()
	numDone = 0
	for order in orders:
		dist = getDist(order[::-1], matrix, distMatrix) # taking advantage of lexigraphic ordering
		if(dist < shortestDistance):
			correctOrder = order
			shortestDistance = dist
	printMatrix(correctOrder, matrix)
	return [correctOrder, shortestDistance]

def getDist(order, matrix, distMatrix):
	global usedList
	dist = 0
	for i in range(0,len(order)):
		whatsLeft = ''.join(str(x) for x in order[i:])
		if (whatsLeft in usedList):
			dist += usedList[whatsLeft]
			break
		else:
			thisDist = 0
			for j in range(i,len(distMatrix[i])):
				thisDist += matrix[order[i]-1][order[j]-1] * distMatrix[i][j]
			usedList[whatsLeft] = thisDist
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

#Assumption! Higher values near the diagonal are more likely to render the solution
def breakAbsoluteSolution(orders, matrix):
	slimmedOrders = list()
	orders = HighestTogether(orders)
	for order in slimmedOrders:
		thisDistMatrix = reorderMatrix(order, matrix)
		if(hasHighestOnDiagonal(thisDistMatrix)):
			slimmedOrders.append(order)
	return slimmedOrders

def highestTogether(orders, matrix):
	i = -1
	values = [sumRow(x, i) for x in matrix]
	values = sorted(values, key = lambda row : row[1])		

def sumRow(row, i):
	i += 1
	return (sum([int(x) for x in row]),i)  

def hasHighestOnDiagonal(distMatrix):
	numToCheck = int(.2 * len(distMatrix))
	itDoes = True
	for i in range(0,len(distMatrix)):
		thisOneDoes = False
		highest = 0
		for el in distMatrix[i]:
			if(highest < el):
				highest = el
		for j in (i-numToCheck,i+numToCheck+1):
			if(j > -1 and j < len(distMatrix)):
				if(distMatrix[i][j] == highest):
					thisOneDoes = True
		itDoes = itDoes and thisOneDoes
	return itDoes
