#!/usr/bin/python3


import sys
import os


# geting a string of and counting the amount of appearances of each character
# and exporing a json file with the results

usage = "USAGE: "+ os.path.basename(sys.argv[0])+" [STRING]"

if len(sys.argv) != 2:
    print(usage)
    sys.exit(1)

if sys.argv[1] == "":
    print(usage)
    sys.exit(1)



str = str(sys.argv[1])
result = {}


#looping over the string and in case the char isnot in the dict i'm adding it and assign to the key the first accurrence 
i = 0
for char in str:
    
    if char not in result:
        result[char] = i
    i = i + 1


print(result)

        
