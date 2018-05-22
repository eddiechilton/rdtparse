import pickle
f = open( 'file.py', 'w' )
with open('data.json', 'r') as myfile:
    searchString = myfile.read()

startWord = 'body'
endWord = '","'
results = []

index = 0
while True:
    try:
        startIndex = searchString.index(startWord, index)
        endIndex = searchString.index(endWord, startIndex)
        results.append(searchString[startIndex + len(startWord):endIndex].strip())
        # move the index to the end
        index = endIndex + len(endWord)

    except ValueError:
         with open("file.py", "wb") as fp:
             pickle.dump(results, fp)
