import csv

my_file = open('Mock_data.csv', 'r+')
csv_f = csv.reader(my_file)
emails = []

for row in csv_f:
    if row:
        emails.append(row[3])

print(emails)

second_file = open('MOCK_DATA-2.csv', 'r+')
csv_2 = csv.reader(second_file)

emails2 = []

for row in csv_2:
    emails2.append(row[3])

print(emails2)

print(len(emails))
print(len(emails2))

emails = set(emails)
emails2 = set(emails2)
print(len(emails))
print(len(emails2))

print(emails.difference(emails2))
print(emails.intersection(emails2))

