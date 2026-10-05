import csv

print("File validation started")
file_path = "C:\Program Files\myproject\script\Python\pythonJVL\DataEngineering\Task 1\employee.csv"

record_count = 0
total_amount = 0
date_validation_failed = False
#read the file
#with sattement automatically manages the file. when python finishes readinf the file, it automatically colese it.
#without  "with" we have to add file.close() to close the file after the reading.
with open(file_path, "r") as my_file:
    print("Hello I'm reading the file")

    reader = csv.DictReader(my_file)

    for row in reader:

        #print(row)

        record_count += 1
        total_amount += float(row["amount"])
        date_value = row["eff_date"]

print("Record count: ", record_count)
print("Total Amount: ", total_amount)

