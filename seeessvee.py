import csv


# Exercise 1
data = [
            ['Top Gun', 'Risky Business', 'Minority Report'],
            ['Titanic', 'The Revenant', 'Inception'],
            ['Training Day', 'Man on Fire', 'Flight']
       ]

with open('file.csv', 'w') as f:
    write = csv.writer(f, delimiter=',')
    for row in data:
        write.writerow(row)

with open('file.csv', 'r') as f:
    read = csv.reader(f, delimiter=",")
    for row in read:
        print(",".join(row))

