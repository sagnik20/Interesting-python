import re
import requests
url = "http://sagnikc.azurewebsites.net/contact/"

EmailRegex = r"[\w\.-]+@[\w\.-]+"
r = requests.get(url)
for match in re.findall(EmailRegex,r.text):
    print(match)