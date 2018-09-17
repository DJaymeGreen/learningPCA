"""
Author: D Jayme Green
Date: 9/16/18
Principal Component Analysis Testing

This is without using numpy's methods. If they were used, it would
only take a few lines of code to do, but I wanted to write it from
scratch myself to fully understand what is happening.
"""

"""
Csv is used to read in the csv data
Numpy is used to allow floats into Matplotlib
"""
import matplotlib.pyplot as mpl
import csv
import math
import numpy as np
import sys;


"""
Constants are declared below for the program
listOfData holds all of the data given
totalNumberOfVals holds the number of rows there is
numberOfCols holds the number of cols there is
"""
listOfData = list(list())
totalNumberOfVals = 0
numberOfCols = 0




"""
Reading in the .csv file and putting it into listOfData which
holds all of the rows as lists. It relies on the file to have
a header on the top
"""
def openCSVFile(fileName):
    listOfData = list()
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        rowNum = 0
        #colNum = len(next(reader))+1
        #for col in range(0,colNum-1):
         #   listOfData.append(list())
        for row in reader:
            listOfData.append(list())
            colNum = len(row)
            for val in range(0,colNum+1):
                try:
                    listOfData[rowNum].append(float(row[val]))
                except:
                    pass
            rowNum += 1
    listOfData.pop(0)
    return listOfData, rowNum, colNum

listOfData, totalNumberOfVals, numberOfCols = openCSVFile('nndb_flat.csv')

"""
Normalizes X to Zero Mean 
For each column: calculate mean and subtract mean from each value in col
"""
def normalizeZeroMean():
    #Find the mean
    colMeans = [0] * len(listOfData[0])
    for row in listOfData:
        for col in range(0,len(row)):
            colMeans[col] += row[col]
    for mean in range(0,len(colMeans)):
        colMeans[mean] /= len(listOfData)

    #Subtract mean from every data point
    for row in range(0,len(listOfData)):
        for col in range(0,len(listOfData[row])):
            listOfData[row][col] -= colMeans[col]
    return listOfData

"""
Finds the covariance matrix of the normalized data
"""
def covarianceMatrix():
    sigma = (1/len(listOfData[0])) * np.dot(np.array(listOfData),np.transpose(np.array(listOfData)))
    #print("Right sigma: " + sigma == np.cov(np.transpose(np.array(listOfData))))
    return sigma

"""
Finds the eigenvectors of the given covariance matrix
I used numpy's built in. There is a lot of math and re-reading to do 
to figure out how to get the eigenvectors and eigenvalues myself
"""
def eigenvectorsOfCovarMatrix(sigma):
    return np.linalg.eig(sigma)

listOfData = normalizeZeroMean()
sigma = covarianceMatrix()
eigenVals, eigenVect = eigenvectorsOfCovarMatrix(sigma)
#The above line causes a memory error. My potato computer needs more RAM for me to continue :/