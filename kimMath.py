#!usr/bin/python3
# quick dirty script to get mean, std, and CI
# i do them so much and dont need to show work, might as well
# it will save lots of time and faffing about

import sys
import numpy as np

filename = sys.argv[1] # get the LOCAL filename
file = open(filename) # open with defaults, 'r'

data_set = [] # dataset to be used
n = 0 # number of items
z = 1.96 # z-score of that interval, im not doing that math

for line in file: # for each line
    n += 1 # increment by one
    data_set.append(int(line)) # add to dataset as an int

mean = round(np.mean(data_set), 3) # get the mean using numpy and round to 3 decimals
print("mean:", mean) # ... you should know this one

std = np.std(data_set) # get strandad deviation, dont round cause used later, want accurate
print("std: ", round(std, 3)) # ... can still round for neatness

confInter = round(z*(std/np.sqrt(n)), 3) # get confidence interval using eqaution from google, then round to 3 places
print(f"95 conf {mean} ± {confInter}") # print, format is mean+-CI, looks nicer, i think, i got the ± to work