"""
This python script reads from sheet2.csv, which contains contact info of people,
then append the data to the respective people in sheet 1.
Author: Pairode Jaroensri
Client: Zoe Ng
Last visited: July 10, 2017
"""

import re
import csv

"""
sheet1.csv is the sheet that is to be added to
sheet2.csv is the sheet that contains the email address, or in this example, cell phone number.
Replace "sheet2.csv" and "sheet1.csv" with your actual csv file names
Replace "Cell" and "Name" with your actual column names
"""

file1 = "sheet1.csv"
file2 = "sheet2.csv"

column_b = "Cell"
column_a = "Name"

scr1 = open(file1, newline='')
field = next(csv.reader(scr1))
scr1.close()
scr1 = open(file1, newline='')
scr2 = open(file2, newline='')

"""
"appended_sheet1.csv" is a new file that will be created.
Feel free to change the file name to something else.
"""
dst = open("appended_sheet1.csv", "w", newline='')

reader2 = csv.DictReader(scr2)
reader1 = csv.DictReader(scr1)


# Lists of dictionaries
table1 = [row for row in reader1]
table2 = [row for row in reader2]
field = field + [column_b]
writer = csv.DictWriter(dst, fieldnames=field)
writer.writerow({col:col for col in field})

i = 1

for row2 in table2:
    name = row2[column_a]
    name_lst = re.split(" +", name)
    firstname = ' '.join([element for element in name_lst[1:] if element[1] != "."])
    lastname = name_lst[0]
    for row1 in table1:
        name1 = row1[column_a]
        name_lst1 = re.split(" +", name1)
        firstname1 = ' '.join([element for element in name_lst1[0:len(name_lst1) - 1] if element[1] != "."])
        lastname1 = name_lst1[-1]
        if firstname == firstname1 and lastname == lastname1:
            print(i, firstname, lastname)
            i += 1
            row1[column_b] = row2[column_b]
            writer.writerow(row1)
            break

scr2.close()
scr1.close()
dst.close()
