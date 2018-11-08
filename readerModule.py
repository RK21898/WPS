###IMPORT SECTION###
import csv
import pandas as pd

def OpenTemperatureModel(f): #create data frame from csv with pandas module
    df=pd.read_csv(f+".csv", names=["Date", "Temperature"],sep=';',parse_dates=[0], na_values=" NaN") #or:, infer_datetime_format=True)
    fileDATES=df.values
    #fileDATES=df.T.to_dict().values() #export the data frame to a python dictionary
    return fileDATES #fileDATES #return the dictionary

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