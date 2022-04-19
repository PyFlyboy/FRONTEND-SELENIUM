import csv

def getCSVData(fileName):

    # create an empty list to store rows
    rows= []
     # Open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV reader from csv data
    reader = csv.reader(dataFile)
    #skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows