#!/usr/bin/env python3

# Script that generates 34 groups (nGroups) each consisting of 24 robot 3-tuples.
# The groups are generated by populating them with random elements from all the
# possible combinations of 18 robots in 3-tuples.

import robotTuples as rT
import matplotlib.pyplot as plt
from random import seed
from collections import Counter

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
iter=0
while iter<nGroups:
    iter=iter+1
    totalTuples=rT.possibleTuples(robots,k)
    currentGroup=rT.generateGroup(totalTuples, groupSize)
    groupsDictionary.update({iter:currentGroup})
    # groupsDictionary.update({'group2':Group2})
    # print(f"DOES THE FOUND SOLUTION FULFILL THE CONSTRAINTS?: {rT.isGroupComplete(currentGroup, n, 4)}")

# print(f"\nThe dictionary with all the groups is:\n {groupsDictionary}")
# print(f"the first group is:  {sorted(groupsDictionary[0])}")

# extracts every robot tuple from dictionary and makes a list
total = groupsDictionary.values()
tupleList = [tuple for group in total for tuple in group]
# print(f"\nThe total list of tuples is: {tupleList}. It has {len(tupleList)} elements.")

# Counts the number of times each tuple appears in the total list:
count = Counter(tupleList)
print(f"\nWe have seen {len(count)} tuples from the {totalCombis} possible ones.")

# x axis: one point per key in the Counter (=unique tuple)
x=range(len(count))

# y axis: count for each tuple, sorted by tuple value
y=[count[key] for key in sorted(count)]

# labels for x axis: tuple as strings
xlabels=[str(t) for t in sorted(count)]

# plot results
plt.bar(x,y,width=0.6)

# set the labels at the middle of the bars
plt.xticks([x+0.5 for x in x],xlabels, rotation = 'vertical')

#show plot
input("Press Enter to show plot...")
plt.show()
