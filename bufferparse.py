import os
directory = "/home/postfreedom/Documents/Reddit_Data/jsonparser/"
moving = open('target.txt', 'w')

def jsonScrape(deltaZ, deltaA, deltaG):
                            ##Writes substrings to objects
    z = x[(x.find(preStringZ)+6):(x.find(searchStringZ, x.find(preStringZ)))-deltaZ]
    a = x[(x.find(preStringA)+12):(x.find(searchStringA, x.find(preStringA)))-deltaA]
    g = x[(x.find(preStringG)+7):(x.find(searchStringG, x.find(preStringG)))-deltaG]
    ##Replaces all commas with '&' symbols to create a well-formatted CSV
    g = g.replace(',', '&')
    ##Writes all objects to CSV comma delimited with line breaks
    moving.write(z +", " + a + ", " + g + "\n")
    ##Disabled Console logs for testing

with open("testdata.json", "r") as currentFile:
        for x in currentFile:
            ##Assign search substrings
            try:
                preStringZ = '"id"'
                searchStringZ = '","'
                preStringA = 'parent_id'
                searchStringA = '","'
                preStringG = 'body'
                searchStringG ='","'
                linebreak = '\n'
                ##Calculate locations of search substrings for comparison
                preZ = x.find(preStringZ)
                preA = x.find(preStringA)
                preG = x.find(preStringG)
                sreZ = x.find(searchStringZ, preZ + 1)
                sreA = x.find(searchStringA, preA + 1)
                sreG = x.find(searchStringG, preG + 1)
                lbki = x.find(linebreak)
                deltaZ = 0
                deltaA = 0
                deltaG = 0
                ##Disabled Console logs for testing
                print(preZ)
                print(preA)
                print(preG)
                print(sreZ)
                print(sreA)
                print(sreG)
                print(lbki)
                ##Check substring order, reassign searchString if line break comes before the next comma
                if sreZ == -1:
                    searchStringZ = linebreak
                    deltaZ = 2
                    jsonScrape(deltaZ, deltaA, deltaG)
                elif sreA == -1:
                    searchStringA = linebreak
                    deltaA = 2
                    jsonScrape(deltaZ, deltaA, deltaG)
                elif sreG == -1:
                    searchStringG = linebreak
                    deltaG = 2
                    jsonScrape(deltaZ, deltaA, deltaG)
                else:
                    jsonScrape(deltaZ, deltaA, deltaG)
                print ('working')
            except ValueError:
                #Disabled Console logs for testing
                print ('something\'s fucky')
