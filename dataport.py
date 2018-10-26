#Imports
import csv

def importCSV(path):
    with open(path, 'r', encoding="utf-8-sig") as csvfile:
        valReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        csvData = [[]]    
        for row in valReader:
            csvData.append(row)
    return csvData

def exportCSV(file, path):
    with open(path, 'wb') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=';',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in file:
            csvWriter.writerow(row)