# rdtparse
hacky data analysis for fun and profit

notes:
5/21
cleaner.py has been running for about a half hour on a moderately sized version of the source object, but it seems to be running properly. may kill and just test on a subset the data if it takes more than a few more hours.

5/22 
gathering source data. todo: refactor counter to take multiple files as input, output results to some file format

5/23
have almost gathered all source files.  individual files run at ~30 gb once extracted, for a total size of ~400gb for the entire source dataset. tried to run counter script on the first extracted file and ran into out-of-memory error. files need to be broken down -- or either small pieces should buffer into memory. metadata per line might be something like -- 

body, sub, ups, score, created_utc, author.  sql? flat? body will be largest piece of data...

if sql: table 1
body, parent_id + ID (unique id?)

parentid+id, parent_id, ID, sub, ups, score, created_UTC, auther

possible slices of data:
top strings by month
top strings aggregate
name strings by month
time series distr on specific strings
top URLs by month
top URLs by sub for certain subs
author time series on specific authors
authors by string

5/24 broke the script to parse the data down to fight memory constraints. source files for jan data are broken into 10mb chunks.  getting very close to having some data to work with (although extracting and unpacking all 11 other files will take a long time)
