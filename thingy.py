# basic script to deal with parsing data from stdout
# has arguments to modify what it reads and where
# want it to be as modular as possible for all stuff
# seems good but could be better
# can choose file, where to start, what to look for that is constant, and offset for data
# want to have it just figure it out, MAGIC

import sys
from itertools import islice

args = sys.argv

filename = args[1] # get file
start_line = args[2] # 53, ..., n where to start, can change based on stuff in file
marker = args[3] # a place in line that is not changed from the line needed, based on spaced and stuff // "Kbits/sec"
infile = open(filename) # file to get data from

print("https://github.com/JoeyShapiro/Manure/blob/master/thingy.py") # sellout :P

offset = int(args[4]) # how far the market is from the item needed, 1 = go back 1 // 1
outfile = open(filename.split(".")[0]+"_formated.rand_ext.png.pdf.txt", 'w') # :P
outfile_dilim = '\n'

for line in islice(infile, int(start_line), None):
    if len(line) < 7: # deal with the extra crap, 7 is the least i can do
        continue
    list_cleaned = line.strip('\n').split(" ")
    lamp = list_cleaned.index(marker) #  // make a variable and thing for
    outfile.write(list_cleaned[lamp-offset]+outfile_dilim) # needs delim

infile.close()
outfile.close()
print("data successfully refined in: " + filename.split(".")[0]+"_formated.rand_ext.png.pdf.txt")