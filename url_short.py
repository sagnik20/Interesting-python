import pyshorteners
a=pyshorteners.Shortener()

print(a.tinyurl.short(input("Enter URL to be Shortened - ")))