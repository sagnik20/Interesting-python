import pandas as pd
import smtplib

df = pd.read_excel("NAME_OF_EXCEL SHEET_CONTAINING_DESTINATION_EMAILID")
emails = df["NAME_OF_COLUMN_CONTAINING_DESTINATION_EMAILID"].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("YOUR_EMAIL","YOUR_PASSWORD")

msg = "Hello this is testing mail for email automation"
subject = "Testing Email Automation"
body = "Subject: {}\n\n{}".format(subject,msg)

for email in emails:
    server.sendmail("YOUR_EMAIL", email, body)

print("Email sended successfuly")
server.quit()
