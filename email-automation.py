
''' If you have not installed pandas and smtplib then open your command prompt or terminal.
    Type pip install pandas to install pandas
    Type pip install smtplib to install smtlib '''

from os import environ
import pandas as pd
import smtplib

# reading excel sheet containing destination email id
df = pd.read_excel("NAME_OF_EXCEL SHEET_CONTAINING_DESTINATION_EMAILID")
emails = df["NAME_OF_COLUMN_CONTAINING_DESTINATION_EMAILID"].values

# passing server address in order to start the server
server = smtplib.SMTP("smtp.gmail.com", 587)

# starting the connections
server.starttls()

# retrieve email and password from environment variables
email = environ['EMAIL']
pw = environ['EMAIL_PW']
# logging in into the server from sender's email id
server.login(email, pw)

# creating body of the email
subject = "Testing Email Automation"
msg = "Hello this is testing mail for email automation"
body = f"""
Subject: {subject}
Message: {msg}
"""

# iterating over the column containing email ids and sending emails to each of id
for email in emails:
    server.sendmail("YOUR_EMAIL", email, body)

# message if email to all ids sent successfuly and stop the server
print("Email sended successfuly")
server.quit()
