import os
directory = ""
moving = open('target.txt', 'w')
with open("testdata.json", "r") as currentFile:
        for x in currentFile:
            try:
                preStringZ = '"id"'
                searchStringZ = '","'
                preStringA = 'parent_id'
                searchStringA = '","'
                preStringG = 'body'
                searchStringG ='","'
                linebreak = '\n'
                preZ = x.find(preStringZ)
                preA = x.find(preStringA)
                preG = x.find(preStringG)
                sreZ = x.find(searchStringZ, preZ + 1)
                sreA = x.find(searchStringA, preA + 1)
                sreG = x.find(searchStringG, preG + 1)
                lbki = x.find(linebreak)
                print(preZ)
                print(preA)
                print(preG)
                print(sreZ)
                print(sreA)
                print(sreG)
                print(lbki)
                if lbki < sreZ:
                    searchStringZ = linebreak
                    if lbki < sreA:
                        searchStringA = linebreak
                        if lbki < sreG:
                            searchStringG = linebreak
                z = x[(x.find(preStringZ)+6):(x.find(searchStringZ, x.find(preStringZ)))]
                a = x[(x.find(preStringA)+15):(x.find(searchStringA, x.find(preStringA)))]
                g = x[(x.find(preStringG)+7):(x.find(searchStringG, x.find(preStringG)))]
                g = g.replace(',', '&')
                moving.write(z +", " + a + ", " + g + "\n")
                print ('working')
            except ValueError:
                print ('something\'s fucky')
