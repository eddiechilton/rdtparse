s = open('data.json','r').read()  # Open the input file

# Program will count the characters in text file
num_chars = len(s)

# Program will count the lines in the text file
num_lines = s.count('\n')

# Program will call split with no arguments
words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

num_words = sum(d[w] for w in d)

lst = [(d[w],w) for w in d]
lst.sort()
lst.reverse()

# stop_words = set(stopwords.words('english'))
# print ([word for word in lst if word not in stop_words])

# Program will print the results
print('Your input file has characters = '+str(num_chars))
print('Your input file has lines = '+str(num_lines))
print('Your input file has the following words = '+str(num_words))

print('\n The 30 most frequent words are /n')

i = 1
for count, word in lst[:10000]:
    print('%2s. %4s %s' %(i,count,word))
    i+= 1
#most of this piece lifted from stack exchange, but will be modified
#todo: refactor for input of 12 files, aggregate reporting, output to some data structure.
