import re
import requests

a = input("Enter Website to scrape Email From -")
url = a

EmailRegex = r"[\w\.-]+@[\w\.-]+"
r = requests.get(url)
for match in re.findall(EmailRegex,r.text):
    print(match)