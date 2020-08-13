#Sentiment analysis by emoji

import emojis
from textblob import TextBlob
v1 = input("Enter your feeling : ")
v = TextBlob(str(v1))
k = v.sentiment
l = k.polarity
#print(l,"\n",k)

if(l == 0.5):
    print(emojis.encode(":heart:"))
elif(v1 == "suicide"):
    print("Be happy dude\t",emojis.encode(":family:"))
elif(l == -0.5):
    print(emojis.encode(":beer:"))
elif(l > 0):
    print(emojis.encode(":smile:"))
elif(l == 0):
    print(emojis.encode(":confused:"))
elif(l < 0):
    print(emojis.encode(":cry:"))