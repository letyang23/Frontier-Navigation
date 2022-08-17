from ai_interface.AIExp import *
from helper_classes.map import *
from time import time

w = 500
l = 500
start = None
goal = None
seed = 0
# AI = Dijkstras()
AI = AStarExp()
# AI = AStarMSH()
filename = None

m = Map(w, l, seed=seed, filename=filename, start=start, goal=goal)
t1 = time()
path = AI.createPath(m)
t2 = time()
print('Time (s): ', t2 - t1)
m.createImage(path)
