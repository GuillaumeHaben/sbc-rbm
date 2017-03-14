import csv
import array

cr = csv.reader(open("result.csv","rb"))

list_action = []

for row in cr:
    
    if row[2] not in list_action:
    	list_action.append(row[2])

list_action.sort()
print list_action