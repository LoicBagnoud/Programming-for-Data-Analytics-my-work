# This program reads the data from a csv file and outputs it to a list

# Author: Loic Bagnoud


import csv

FILENAME = "data.csv"


# Opens the CSV file which is in the variable FILENAME
with open (FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")

    #The line count will be 0
    linecount = 0
    total = 0

    # We create a for loop that goes into the reader and if the linecount is 0, then we skip (pass)
    for line in reader:
        if not linecount:  
            pass
        #Otherwise, the total starts from the first line (now changed to be calculated as an integer)
        else: 
            total += int(line[1])
        linecount += 1

    print(f"average is {total/(linecount)-1}")

# Another alternative

with open(FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
# print (line)
        count +=1
print (f"average is {total/(count)}") 