import wikipedia

query = input("Enter Search term: ")
try:
    page = wikipedia.page(query)
    print(page.summary, sentences = 2)
except:
    topics = wikipedia.search(query)
    print(f"Search results for {query} :")
    for i, topic in enumerate(topics):
        print (f"{i}. {topic}")
    choice = int(input("Enter a choice: "))
    assert choice in range(len(topics))
    result = wikipedia.summary(topics[choice] , sentences = 2)
    print(result)
