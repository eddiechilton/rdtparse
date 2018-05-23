# rdtparse
hacky data analysis for fun and profit

notes:
5/21
cleaner.py has been running for about a half hour on a moderately sized version of the source object, but it seems to be running properly. may kill and just test on a subset the data if it takes more than a few more hours.

5/22 
gathering source data. todo: refactor counter to take multiple files as input, output results to some file format

5/23
have almost gathered all source files.  individual files run at ~30 gb once extracted, for a total size of ~400gb for the entire source dataset. tried to run counter script on the first extracted file and ran into out-of-memory error. files need to be broken down -- or either small pieces should buffer into memory
