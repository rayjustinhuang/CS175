from numpy import random
import matplotlib.pyplot as plt

# BALL-PICKING ENGINE
# Given a number of balls and a number of red, white, and black balls, generates a list of drawn balls
# of the format [reds, whites, blacks]

def BallPicker(take=3, red=7, white=5, black=8):
    SetofBalls = [0,0,0]
    for run in range(take):
        TotalBalls = red + white + black
        seed = random.randint(1,TotalBalls+1)
        if seed > red + white:
            SetofBalls[2] += 1
            black -= 1
        elif seed > red:
            SetofBalls[1] += 1
            white -= 1
        else:
            SetofBalls[0] += 1
            red -= 1
    return tuple(SetofBalls)

print(BallPicker(3))
%%timeit -n 100

# ONE OF EACH
# Given a number of runs, returns the number of times the resulting draw turned out to have
# one of each colored ball. Assumes 3 balls are drawn from the bag.

def OneOfEach(runs):
    DesiredOutcomes = 0
    for i in range(runs):
        result = BallPicker()
        if result == (1,1,1):
            DesiredOutcomes += 1
    return DesiredOutcomes/runs

# print([10**x for x in range(1,7)])
# print(OneOfEach(10))
# print(OneOfEach(100))
# print(OneOfEach(1000))
# print(OneOfEach(10000))
# print(OneOfEach(100000))
# print(OneOfEach(1000000))

# AT LEAST ONE RED
# Given a number of runs, returns the number of times the resulting draw turned out to have
# one of each colored ball. Assumes 3 balls are drawn from the bag.

def AtLeastOneRed(runs):
    DesiredOutcomes = 0
    for i in range(runs):
        result = BallPicker()
        if result[0] >= 1:
            DesiredOutcomes += 1
    return DesiredOutcomes/runs

# print(AtLeastOneRed(10))
# print(AtLeastOneRed(100))
# print(AtLeastOneRed(1000))
# print(AtLeastOneRed(10000))
# print(AtLeastOneRed(100000))
# print(AtLeastOneRed(1000000))

# Plotting in a bar chart
# xaxis = [10**x for x in range(1,7)] + [5*(10**x) for x in range(1,6)]
xaxis = [i*10 for i in range(1,10)] + [i*100 for i in range(1,10)] + [i*1000 for i in range(1,10)] + [10**x for x in range(4,7)] + [5*(10**x) for x in range(4,6)]
xaxis.sort()
yaxis1 = [ OneOfEach(xaxis[i]) for i in range(len(xaxis)) ]
xaxislabels = [str(xaxis[i]) for i in range(len(xaxis))]

print(xaxislabels)
barwidths = [i for i in range(len(xaxis))]


plt.bar(barwidths, yaxis1, color='green')

plt.ylabel("Probability")
plt.xlabel("Draws")
plt.title("Simulated Probability of Picking One of Each vs. Number of Draws")
plt.xticks([i for i in range(len(xaxislabels))], xaxislabels, rotation="45")
plt.autoscale()
x1,x2,y1,y2 = plt.axis()
plt.axis([x1,x2,0,1])
plt.show()

# Second plot

yaxis2 = [ AtLeastOneRed(xaxis[i]) for i in range(len(xaxis)) ]

plt.bar(barwidths, yaxis2, color='green')

plt.ylabel("Probability")
plt.xlabel("Draws")
plt.title("Simulated Probability of Getting at Least One Red vs. Number of Draws")
plt.xticks([i for i in range(len(xaxislabels))], xaxislabels, rotation="45")
plt.autoscale()
x1,x2,y1,y2 = plt.axis()
plt.axis([x1,x2,0,1])
plt.show()