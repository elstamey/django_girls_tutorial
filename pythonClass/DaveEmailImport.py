import csv

emails =[]

with open('MOCK_DATA.csv', 'r') as data:
    reader = csv.DictReader(data)
    [emails.append(x['email']) for x in reader if x]

print(emails)