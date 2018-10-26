#Imports
import csv

def importCSV(path):
    with open(path, 'rb') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    csvFile = importCSV(path)
    csvHeaders, csvData = []
    for column in valreader:
        csvHeaders.append(column)
    for row in valreader
        csvData.append(row)

def exportCSV(file, path):
    with open(path, 'wb') as csvfile:
        csvWriter = csv.writer(file, delimiter=' ',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in file:
            csvWriter.writerow(row)