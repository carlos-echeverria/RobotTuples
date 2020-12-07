#!/usr/bin/env python3

# Script that generates 34 groups (nGroups) each consisting of 24 robot 3-tuples.
# The groups are generated by populating them with random elements from all the
# possible combinations of 18 robots in 3-tuples.

import robotTuples as rT
import matplotlib.pyplot as plt
from collections import Counter
from random import seed
from datetime import datetime

n = 18 # total number of robots
k = 3  # number of robots per tuple
groupSize = 24 # number of tuples per group
nGroups = 34 # number of groups desired

# creates list of robots:
robots = list(range(1,n+1))

# generates all the possible tuples with the above given parameters:
totalTuples = rT.possibleTuples(robots,k)
totalCombis = len(totalTuples) # number of available tuples to choose from

print(f"\nWith {n} robots, there are {totalCombis} posible combinations of {k}-tuples.\n\nWe will construct {nGroups} groups of {k}-tuples, each consisting of {groupSize} elements.\n\nEvery robot should appear {4} times in each group.")

# initializes dictionary where groups will be stored:
groupsDictionary = {}

# generates groups using the functions available in the file 'robotTuples.py'
iter=1
countr=0
while iter<nGroups:
    # creates all possible tuples defined by the parameters from above:
    totalTuples=rT.possibleTuples(robots,k)
    # generates a group which fulfills the constraints:
    currentGroup=rT.generateGroupInSilence(totalTuples, groupSize)
    # add the created group to a dictionary:
    groupsDictionary.update({iter:currentGroup})
    # extracts every robot tuple from dictionary then makes a list:
    total = groupsDictionary.values()
    tupleList = [tuple for group in total for tuple in group]
    # print(f"\nThe total list of tuples is: {tupleList}. It has {len(tupleList)} elements.")
    old_countr=countr
    # Counts the number of times each tuple appears in the total list:
    count = Counter(tupleList)
    countr = len(count)
    print(f"\nWe have found {countr} tuples from the {totalCombis} possible ones. So far we have created {iter+1} groups.\n")
    if countr >= old_countr+20:
        iter=iter+1
    else:
        groupsDictionary.pop(iter)
        countr = old_countr


## Saving output of experiment

# gets the current date and time to generate a unique filename for storing results:
now = datetime.now()
date1 = now.strftime("%Y:%m:%d")
date2 = now.strftime("%Y/%m/%d")
time = now.strftime("%H:%M:%S")


# prints resulting groups to unique file with human readable format:
with open(f"Results-{date1}-{time}.txt", 'w+') as file:
    file.write(f"The following groups were created on {date2} at {time}.\n")
    for i in range(1,nGroups+1):
        file.write(f"\n Group {i}: {groupsDictionary[i]}\n")


# prints resulting groups to another unique file for javascript experiment:
with open(f"Results-{date1}-{time}_js.txt", 'w+') as file:
    for i in range(1,nGroups+1):
        file.write(f"\n---------Group{i}---------\n")
        for tuple in groupsDictionary[i]:
            idx = groupsDictionary[i].index(tuple)
            file.write(f"var set{idx+1} = {list(tuple)};\n")


# Saving output of experiment
print(f"\nDid this work?.\n")

# 0
# 24
# 48
# 72
# 96
# 120
# 144
# 168
# 192
# 216
# 240
# 264
# 288
# 312
# 336
# 360
# 384
# 408
# 432
# 456
# 480
# 504
# 528
# 552
# 576
# 600
# 624
# 648
# 672
# 696
# 720
# 744
# 768
# 792
