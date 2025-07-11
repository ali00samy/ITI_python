import os
import csv
from email_validation import validate
import email_domains

file_name = "Tasks\Emails.csv"
file_path = os.path.join(os.getcwd(), file_name)

emails = []

if os.path.exists(file_path):
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip first row

        for row in reader:
            if row:  # make sure row is not empty
                emails.append(row[-1])  # last column assumed to be email

    valid_emails = list(filter(validate, emails))
    print(valid_emails)

    email_domains.get_domains(emails)

else:
    print("File not found.")
