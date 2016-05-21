import csv

fileName = 'MOCK_DATA.csv'
csvFile = open(fileName, 'r')
reader = csv.reader(csvFile)

columnValues = []
headerName = 'email'

headerNames = next(reader)
columnIndex = headerNames.index(headerName)

#print(columnIndex)
#print(headerNames[columnIndex])

for row in reader:
    if row:
        columnValue = row[columnIndex]
        columnValues.append(columnValue)

print(columnValues)