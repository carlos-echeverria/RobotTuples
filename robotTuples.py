#!/usr/bin/env python3

# Library of functions to find tuples from a list of elements (robots) intended
# for preparing a Best-Worst scaling comparison.

from itertools import combinations
from collections import Counter, defaultdict
from random import choice, choices, seed, sample


def possibleTuples(robots,k):
    # Return a list of all tuples of length k form a list of robots of size n.
    return list(combinations(robots,k))


def addTupleToGroup(totalTuples,group,discarded):
    # Given a list of robot 3-tuples and two groups with or without elements,
    # the function adds a tuple to the group only if the individual robot count
    # does not exceed 4, i.e., only if the desired constraints are met).
    # Warning: function assumes 3-tuples and a totla of 18 robots.
    try:
        randTuple = choice(totalTuples)

        group.append(randTuple)
        groupL = [robot for tupl in group for robot in tupl]
        cnt = Counter(groupL)
        robotsInGroup = list(cnt.keys())
        if (cnt[1]<=4 and cnt[2]<=4 and cnt[3]<=4 and cnt[4]<=4 and cnt[5]<=4 and cnt[6]<=4 and cnt[7]<=4 and cnt[8]<=4 and cnt[9]<=4 and cnt[10]<=4 and cnt[11]<=4 and cnt[12]<=4 and cnt[13]<=4 and cnt[14]<=4 and cnt[15]<=4 and cnt[16]<=4 and cnt[17]<=4 and cnt[18]<=4):
            try:
                idx = totalTuples.index(randTuple)
                totalTuples.pop(idx)
            except IndexError:
                print("Index error... No more tuples in group.")
        else:
            discarded.append(group.pop())
            idx = totalTuples.index(randTuple)
            totalTuples.pop(idx)

    except IndexError:
        print("No more tuples left in list of all possible tuples after first run.")


def generateGroup(totalTuples, groupSize):
    # Given a list of robot tuples and a group size, the function generates
    # a group of tuples of the given size which fulfill the desired constraints,
    # i.e., each robot appears 4 times in the group.
    iter=0
    group=[]
    discarded=[]
    # convergenceFlag=0
    totalCombis=len(totalTuples)
    while len(group)<groupSize or iter<totalCombis: #and convergenceFlag!=1:
        iter=iter+1
        addTupleToGroup(totalTuples, group, discarded)
        groupList = [robot for tuple in group for robot in tuple]
        robotCounter = Counter(groupList)

        if (len(group)==groupSize):
            print(f"\nThe following group was generated fulfilling the desired constraints:\n {sorted(group)}.")
            # print(f"\nTHE FOLLOWING GROUP WAS CREATED WITH THE DESIRED CONSTRAINTS:\n {group}.")
            # convergenceFlag=1
            return group

        if (iter==totalCombis):
            # print("\nERROR: A GROUP COULD NOT BE BUILT WITH THE GIVEN SETS...TRYING AGAIN.\n")
            totalTuples=totalTuples+group+discarded
            iter=0
            group=[]
            discarded=[]
            # convergenceFlag=0


def countElementsInGroup(group):
    # Given a group of robots (list of tuples), the function counts the number
    # of times each robot appears in the group.
    c = Counter()
    for t in group:
        c.update(t)
    return c


def isGroupComplete(group, groupSize, nRobots):
    # Given a group of robots (list of tuples), a group size and the number of
    # times each robot should appear in the group, the function returns a
    # true/false statement if the group fulfills the constraints.
    c = countElementsInGroup(group)

    valid = (len(c) == groupSize)
    for n in c.values():
        valid &= (n == nRobots)
    return valid


def pairKey(pair):
    # Given a pair of tuples, the function returns a key which identifies the
    # tuples by the members it posseses.
    return tuple(sorted(list(pair[0]) + list(pair[1])))


def buildPairsDict(availableTuples):
    # Given the list of all available tuples, the function creates a dictionary
    # of the form:
    #   key = the set of elements in the two tuples
    # value = the list of tuple pairs that correspond to the key

    tuplesPairs = defaultdict(list)
    for pair in combinations(availableTuples, 2):
        key = pairKey(pair)
        tuplesPairs[key].append(pair)
    return tuplesPairs


def shufflePairOfElements(currentGroup, allTuples):
    # Given a tuple group and a list of all available tuples, the function
    # selects two tuples at random, looks it up in the dictionary, and picks
    # another pair if there is one

    # Make a copy, I want to avoid modifying the input:
    currentGroup = set(currentGroup)

    availableTuples = set(allTuples) - set(currentGroup)
    availableTuplesPairs = buildPairsDict(availableTuples)

    # Pick two tuples at random:
    replaceTuples = sample(currentGroup, k=2)

    # Pick two tuples with the same elements to replace them:
    availableMatchingTuples = availableTuplesPairs[pairKey(replaceTuples)]
    if len(availableMatchingTuples) == 0:
        # No tuples available: do nothing
        return currentGroup

    newTuples = choice(availableMatchingTuples)
    print(f"We will replace these tuples: {replaceTuples},")
    print(f"with these tuples: {newTuples}.")

    # Replace old tuples with new tuples:
    currentGroup.remove(replaceTuples[0])
    currentGroup.remove(replaceTuples[1])
    currentGroup.add(newTuples[0])
    currentGroup.add(newTuples[1])

    return currentGroup
