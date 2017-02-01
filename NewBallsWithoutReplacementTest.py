from numpy import random

def BallPicker(take=3, red=7, white=5, black=8):
    R, W, B = 0, 0, 0
    for run in range(take):
        TotalBalls = red + white + black
        seed = random.randint(1,TotalBalls+1)
        if seed > red + white:
            B += 1
            black -= 1
        elif seed > red:
            W += 1
            white -= 1
        else:
            R += 1
            red -= 1
    return (R,W,B)

print(BallPicker())