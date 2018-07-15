import os
directory = "/home/eddie/Documents/projects/rdtparse"
moving = open('target.txt', 'w')
preStringZ = '"id"'
preStringA = 'parent_id'
preStringG = 'body'
preStringK = 'created_utc'
preStringE = 'ups'
preStringX = '"author"'
preStringP = 'subreddit_id'


def jsonScrape (deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP):
                            ##Writes substrings to objects
    global x
    z = x[(x.find(preStringZ)+7):(x.find(searchStringZ, x.find(preStringZ)))-deltaZ]
    a = x[(x.find(preStringA)+12):(x.find(searchStringA, x.find(preStringA)))-deltaA]
    g = x[(x.find(preStringG)+7):(x.find(searchStringG, x.find(preStringG)))-deltaG]
    k = x[(x.find(preStringK)+13):(x.find(searchStringK, x.find(preStringK)))-deltaK]
    e = x[(x.find(preStringE)+5):(x.find(searchStringE, x.find(preStringE)))-deltaE]
    x = x[(x.find(preStringX)+10):(x.find(searchStringX, x.find(preStringX)))-deltaX]
    p = x[(x.find(preStringP)+15):(x.find(searchStringP, x.find(preStringP)))-deltaP]
    ##Replaces all commas with '&' symbols to create a well-formatted CSV
    g = g.replace(',', '&')
    ##Writes all objects to CSV comma delimited with line breaks
    moving.write(z + ", " + a + ", " + g + ", " + k + ", " + e + ", " + x + ", " + p +"\n")

    ##Disabled Console logs for testing
    #THIS IS WHAT I CANT FIGURE OUT!
    print ("subreddit_id: " + p)
    ##this index shouldn't equal -1:
    print(x.find(preStringP))

with open("rc06oneline.json", "r") as currentFile:
        for x in currentFile:
            ##Assign search substrings
            try:
                ##values of '","' work with strings, values of ',"' work with ints
                searchStringZ = '","'
                searchStringA = '","'
                searchStringG = '","'
                searchStringK = ',"'
                searchStringE = ',"'
                searchStringX = '","'
                searchStringP = '","'
                linebreak = '\n'
                #Calculate locations of search substrings for comparison
                preZ = x.find(preStringZ, 0)
                preA = x.find(preStringA, 0)
                preG = x.find(preStringG, 0)
                preK = x.find(preStringK, 0)
                preE = x.find(preStringE, 0)
                preX = x.find(preStringX, 0)
                preP = x.find(preStringP, 0)
                sreZ = x.find(searchStringZ, preZ + 1)
                sreA = x.find(searchStringA, preA + 1)
                sreG = x.find(searchStringG, preG + 1)
                sreK = x.find(searchStringK, preK + 1)
                sreE = x.find(searchStringE, preE + 1)
                sreX = x.find(searchStringX, preX + 1)
                sreP = x.find(searchStringP, preP + 1)
                lbki = x.find(linebreak)
                deltaZ = 0
                deltaA = 0
                deltaG = 0
                deltaK = 0
                deltaE = 0
                deltaX = 0
                deltaP = 0
                ##Disabled Console logs for testing
                # print(preZ)
                # print(preA)
                # print(preG)
                # print(sreZ)
                # print(sreA)
                # print(sreG)
                # print(lbki)
                # print(preP)
                # print(sreP)
                ##Check substring order, reassign searchString if line break comes before the next comma
                if sreZ == -1:
                    searchStringZ = linebreak
                    deltaZ = 2
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                elif sreA == -1:
                    searchStringA = linebreak
                    deltaA = 2
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                elif sreG == -1:
                    searchStringG = linebreak
                    deltaG = 2
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                elif sreK == -1:
                    searchStringK = linebreak
                    deltaK = 2
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                elif sreE == -1:
                    searchStringE = linebreak
                    deltaE = 2
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                elif sreX == -1:
                    searchStringX = linebreak
                    deltaX = 2
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                    print('sreX==-1')
                elif sreP == -1:
                    searchStringP = linebreak
                    deltaP = 2
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                    print('sreP==-1')
                else:
                    jsonScrape(deltaZ, deltaA, deltaG, deltaK, deltaE, deltaX, deltaP)
                    print("normal")
                print ('working')
            except ValueError:
                #Disabled Console logs for testing
                print ('something\'s fucky')
        print("done")
