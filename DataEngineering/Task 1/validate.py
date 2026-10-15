import csv
import logging
import sys
from datetime import datetime

print("File validation started")
file_path = "C:\Program Files\myproject\script\Python\pythonJVL\DataEngineering\Task 1\employee.csv"
ctl_path = "C:\Program Files\myproject\script\Python\pythonJVL\DataEngineering\Task 1\employee.ctl"

#Logging Config
logging.basicConfig(
    filename= "validation.log",
    level = logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("File validation started")

#initialization
record_count = 0
total_amount = 0
date_validation_failed = False
validation_failed = False

#r for read the file
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
        try:
            datetime.strptime(date_value, "%d-%b-%Y") #%d- Day (two digit), %b- month (Oct, May), %Y- Four digit year (2026)
            print("Valid date : ", date_value)
        except ValueError:
            date_validation_failed = True
            validation_failed = True
            print("Invalid date : ", date_value)
            logging.error("Invalid date: %s", date_value)

    if date_validation_failed:
        print("Dates are failed due to validation")
        logging.error("Date Validation FAILED")
    else:
        print("All Dates are valid")
        logging.info("Date Validation PASSED")



print("Record count: ", record_count)
print("Total Amount: ", total_amount)

logging.info("Record count: %s", record_count)
logging.info("Total Amount: %s", total_amount)

#CTL file  reading 

with open(ctl_path,"r",encoding="utf-8-sig") as ctl_file:

          expect_count = int(ctl_file.readline().strip())          
          expect_amount = float(ctl_file.readline().strip())

# Display expected values
print("Expected record count:", expect_count)
print("Expected total amount:", expect_amount)

#Compare 
if record_count == expect_count:
    print("Record count is mismatched")
    logging.error("record count MISMATCHed")
else:
    print("Record count MISMATCHED")
    logging.error("Record count MISMATCHED")
    validation_failed = True

if total_amount == expect_amount:
    print("Total amount MATCHED")
    logging.info("Total amount MATCHED")
else:
    print("Total amount MISMATCHED")
    logging.error("Total amount MISMATCHED")
    validation_failed = True

#Final 
if validation_failed:
    print("FILE VALIDATION FAILED")
    logging.error("FILE VALIDATION FAILED")
    sys.exit(1)
else:
    print("FILE VALIDATION PASSED")
    logging.info("FILE VALIDATION PASSED")
    sys.exit(0)