import os
directory = "/home/postfreedom/Documents/Reddit_Data/Data/jan16"
for filename in os.listdir(directory):
    if filename.startswith("x"):
        print(os.path.join(directory, filename))
    else:
        print 'done'
