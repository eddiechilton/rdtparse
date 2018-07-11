import os
directory = "/home/postfreedom/Documents/Reddit_Data/jsonparser/"
moving = open('target.txt', 'w')
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
                ##Disabled Console logs for testing
                # print(preZ)
                # print(preA)
                # print(preG)
                # print(sreZ)
                # print(sreA)
                # print(sreG)
                # print(lbki)
                ##Check substring order, reassign searchString if line break comes before the next comma
                if lbki < sreZ:
                    searchStringZ = linebreak
                    if lbki < sreA:
                        searchStringA = linebreak
                        if lbki < sreG:
                            searchStringG = linebreak
                ##Writes substrings to objects
                z = x[(x.find(preStringZ)+6):(x.find(searchStringZ, x.find(preStringZ)))]
                a = x[(x.find(preStringA)+15):(x.find(searchStringA, x.find(preStringA)))]
                g = x[(x.find(preStringG)+7):(x.find(searchStringG, x.find(preStringG)))]
                ##Replaces all commas with '&' symbols to create a well-formatted CSV
                g = g.replace(',', '&')
                ##Writes all objects to CSV comma delimited with line breaks
                moving.write(z +", " + a + ", " + g + "\n")
                ##Disabled Console logs for testing
                # print ('working')
            except ValueError:
                ##Disabled Console logs for testing
                # print ('something\'s fucky')
                ##Note: Data should be tested for completeness as well as correctl functionality
