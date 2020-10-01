import wikipedia # Please install the python package wikipedia before with "pip3 install wikipedia"

query = input("Enter Search term: ") # Prompt the user to enter the search term
try: # Try block to check for error
    page = wikipedia.page(query) # Load the page for the search term
    print(page.summary, sentences = 2) # Print the 1st 2 lines of the summary
except: # handle error if it occurs
    topics = wikipedia.search(query) # Load a list of items that match the user input
    print(f"Search results for {query} :")
    for i, topic in enumerate(topics): # Generate a menu from the search results
        print (f"{i}. {topic}") # Using formated string to display in desired order of index followed by result
    choice = int(input("Enter a choice: ")) # Prompt user to select desired item by their index
    assert choice in range(len(topics)) # To avoid IndexOutOfBound Exception
    result = wikipedia.summary(topics[choice] , sentences = 2) # Stroing the summary in a variable for better code readability
    print(result)
