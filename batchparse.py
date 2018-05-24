import os
directory = "/home/postfreedom/Documents/Reddit_Data/Data/jan16/"
moving = open('target.txt', 'w')
for y in os.listdir(directory):
    if y.startswith("x"):
        with open(y, "r") as currentFile:
            for x in currentFile:
                a = x[(x.index('parent_id')+9):(x.index('","'))]
                g = x[(x.index('"id"')+4):(x.index('","'))]
                z = x[(x.index('body')+4):(x.index('","'))]
                # # moving.write(z + "\n" + a +"\n")
                # # # y.close()
                moving.write(z +"\n" + a + "\n" + g)

            else:
                # moving.close()
                print 'failure'
