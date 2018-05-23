f = open( 'jan16out.txt', 'w' )
with open("jan16.txt") as f:
    line = f.readline()
    i = 0
    startWord = 'body'
    endWord = '","'
    for line in f:
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
        with open("jan16out.txt", "a") as myfile:
            myfile.write(results +'\n')

i = 1
for count, word in lst[:10000]:
    print('%2s. %4s %s' %(i,count,word))
    i+= 1
