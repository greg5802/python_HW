#1/2
import os

import csv

csvpath = os.path.join('PyBank','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)

    for row in csvreader:
        #print(csvreader)
        count_row = sum(1 for row in csvreader)
        print("Total Months:",count_row)


csvpath = os.path.join('PyBank','budget_data.csv')

#rand_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csvreader:
        #print(csvreader)
        total = int(row[1]) -total

    print("Total Value:",total)

average = round(total/count_row)
print("Average:",average)


csvpath = os.path.join('PyBank','budget_data.csv')

rand_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        rand_list.append(int(row[1]))
        max_num = max(rand_list)

    print("Maximum:",max_num)


csvpath = os.path.join('PyBank','budget_data.csv')

rand_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        rand_list.append(int(row[1]))
        min_num = min(rand_list)

    print("Minimum:",min_num)
