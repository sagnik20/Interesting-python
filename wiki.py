import wikipedia
a = input("Enter Words to Search - ")

result = wikipedia.summary(a, sentences=2)
print(result)
