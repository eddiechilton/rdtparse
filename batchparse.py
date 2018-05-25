import os
directory = "/home/postfreedom/Documents/Reddit_Data/Data/jan16/"
moving = open('target.txt', 'w')
preStringZ = '"id"'
searchStringZ = '","'
preStringA = 'parent_id'
searchStringA = '","'
preStringG = 'body'
searchStringG ='","'
for y in os.listdir(directory):
    if y.startswith("x"):
        with open(y, "r") as cuhttps://news.google.com/?hl=en-US&gl=US&ceid=US:enrrentFile:
            for x in currentFile:
                z = x[(x.index(preStringZ)+6):(x.index(searchStringZ, x.index(preStringZ)))]
                a = x[(x.index(preStringA)+15):(x.index(searchStringA, x.index(preStringA)))]
                g = x[(x.index(preStringG)+7):(x.index(searchStringG, x.index(preStringG)))]
                # moving.write(z + "\n" + a +"\n")
                # # y.close()
                moving.write(z +"\n" + a + "\n" + g + "\n")
                print z
                print a
                print g
                print y
            # else:
            #     # moving.close()
            #     print 'failure'

