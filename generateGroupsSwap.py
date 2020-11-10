
import sys
import robotTuples as rT
from random import seed
import matplotlib.pyplot as plt
from collections import Counter

n = 18 # number of robots
k = 3  # tuple size
robots = list(range(1,n+1))
groupSize = 24
totalTuples = rT.possibleTuples(robots,k)
totalCombis = len(totalTuples)

print(f"\nWith {n} robots, there are {totalCombis} posible combinations of {k}-tuples.\n")

Group1 = rT.generateGroup(totalTuples, groupSize)

CurrentGroup = set(Group1)
print(f"Is the first solution a complete group?: {rT.isGroupComplete(CurrentGroup, n, 4)}")

shuffleTimes = 100
for itr in range(shuffleTimes):
    if (itr%10==0):
        print(f'--{itr}--')
    CurrentGroup = rT.shufflePairOfElements(CurrentGroup, totalTuples)
    ###print('----')
    if itr == shuffleTimes-1:
        #print(f"There were {cntr} shuffles made.")
        print(f"The next found solution is:\n {sorted(CurrentGroup)}.")
        print(f"Is the next found solution a complete group?: {rT.isGroupComplete(CurrentGroup, n, 4)}")


Total =  Group1
for x in CurrentGroup:
    Total.append(x)

kntr = Counter(Total)
# x axis: one point per key in the Counter (=unique tuple)
x=range(len(kntr))
print(f"We have seen {len(kntr)} tuples from the possible {totalCombis}")
# y axis: count for each tuple, sorted by tuple value
y=[kntr[key] for key in sorted(kntr)]
# labels for x axis: tuple as strings
xlabels=[str(t) for t in sorted(kntr)]

# plot
plt.bar(x,y,width=0.6)
# set the labels at the middle of the bars
plt.xticks([x+0.5 for x in x],xlabels, rotation = 'vertical')
plt.show()
