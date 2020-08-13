from googlesearch import search
query = "python" #the text you want to search
#tld refers to the top level domain like .com or .in
#num refers to the number of results we want
for i in search(query,tld = "com", num=10, stop=10, pause=2):
    print(i)