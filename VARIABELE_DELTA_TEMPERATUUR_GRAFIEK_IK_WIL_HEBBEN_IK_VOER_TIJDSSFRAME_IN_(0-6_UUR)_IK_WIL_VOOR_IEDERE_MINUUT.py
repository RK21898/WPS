from datetime import datetime, timedelta
import time
import csv

startDate = time.strftime("%x")
startHours = [3, 7, 22]
endHours = [5, 12, 23]
path = 'AllDayFormat.csv'
wantedTemp = 21

def createCSV(startDate, startHours, endhours, path):
    dtf = createDTF(startDate)
    with open(path, 'w') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',')
        for row in dtf:
            written = 0
            userTimes = 0
            tempDatetime = datetime.strptime(row, '%Y-%m-%d %H:%M')
            while (userTimes < len(startHours)):
                if(tempDatetime >= datetime(2018, 11, 6, startHours[userTimes]) and tempDatetime <= datetime(2018, 11, 6, endhours[userTimes])):                
                    csvWriter.writerow([row, wantedTemp])
                    written = 1
                userTimes += 1  
            if (written == 0):
                csvWriter.writerow([row])
                


def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

def createDTF(startDate):
    dtf = [dt.strftime('%Y-%m-%d %H:%M') for dt in 
        datetime_range(datetime(2018, 11, 6, 0), datetime(2018, 11, 6, 23, 59, 59), 
        timedelta(minutes=1))]
    return dtf

#Test
createCSV(startDate, startHours, endHours, path)