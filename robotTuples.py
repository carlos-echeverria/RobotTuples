#!/usr/bin/env python3

import sys
from itertools import combinations
from random import choice
from random import seed
from collections import Counter

n = 9 # number of robots
k = 3  # tuple size
robots = list(range(1,n+1)) 
groupSize = 12
seed(2)


def possibleSets(robots,k):
    # return list of all subsets of length k form the n-element array robots.
    return list(combinations(robots,k))


def addElementToGroup(totalSets,Group,discarded):
    # add element if constraints are met
    try:
        rElement = choice(totalSets)
        #rElement = totalSets[0]
        print("We choose a random element from the possible 3-tuples: {}.".format(rElement))

        Group.append(rElement)
        GroupL = [x for tup in Group for x in tup]
        cnt = Counter(GroupL)
        robotsInGroup = list(cnt.keys())
        if (cnt[1]<=4 and cnt[2]<=4 and cnt[3]<=4 and cnt[4]<=4 and cnt[5]<=4 and cnt[6]<=4 and cnt[7]<=4 and cnt[8]<=4 and cnt[9]<=4 and cnt[10]<=4 and cnt[11]<=4 and cnt[12]<=4 and cnt[13]<=4 and cnt[14]<=4 and cnt[15]<=4 and cnt[16]<=4 and cnt[17]<=4 and cnt[18]<=4):

            try:
                idx = totalSets.index(rElement)
                totalSets.pop(idx)
            except IndexError:
                print("error")
        else:
            discarded.append(Group.pop())
            idx = totalSets.index(rElement)
            totalSets.pop(idx)


    except IndexError:
        print("no more elements in first run")
        addElementToGroup(discarded, Group, discarded=[])


totalSets = possibleSets(robots,k)
totalCombis = len(totalSets)


print("\nWith {} robots, there are {} posible combinations of {}-tuples.\n".format(n, totalCombis, k))


iter=0#
Group1=[]
discarded=[]
while len(Group1)<groupSize and iter<totalCombis:
    iter=iter+1
    #print("Total Sets Remaining before iteration: {}".format(len(totalSets)))
    print("Iteration: {}".format(iter))
    print("Number of Sets Remaining before adding a new element: {}".format(len(totalSets)))
    print("The group before adding a new element is:\n {}.".format(Group1))
    addElementToGroup(totalSets, Group1, discarded)
    print("The group after adding a new element is:\n {}.".format(Group1))
    Group1L = [x for tup in Group1 for x in tup]
    cntT = Counter(Group1L)
    print("Group element {}.".format(cntT))
    print("Number of Sets Remaining after iteration: {}.".format(len(totalSets)))
    #print("Sets Remaining:\n {}".format(totalSets))
    print("Number of Sets Discarded so far: {}.".format(len(discarded)))
    #print("Sets Discarded:\n {}.".format(discarded))
    print("\n")
    if (len(Group1)==groupSize):
        print("GROUP WAS CREATED WITH THE DESIRED CONSTRAINTS.\n")
        totalSets=totalSets+discarded
    if (iter==totalCombis):
        print("\nERROR: A GROUP COULD NOT BE BUILT WITH THE GIVEN SETS.\n")
        quit()
