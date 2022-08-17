import math

from ai_interface.AIModule import *


def chebychev(n0, n1):
    return max(abs(n0.x - n1.x), abs(n0.y - n1.y))


def heuristic(node, goal, map_):
    delta_h = map_.getTile(goal.x, goal.y) - map_.getTile(node.x, node.y)
    d = chebychev(node, goal)

    # delta_h > 0 up the hill
    if delta_h > 0:
        h = math.pow(math.e, 1) * delta_h
    # delta_h < 0 down the hill
    elif delta_h < 0:
        slope = delta_h / d
        h = math.pow(math.e, slope) * d
    else:  # delta_h = 0 same height
        h = d
    return h


class AStarExp(AIModule):

    def createPath(self, map_):
        q = PriorityQueue()
        ''' Maintain three dictionaries to keep track of cost ("x,y" -> cost per
        node), previous (node -> parent). This keeps track of paths, and explored
        which helps us run faster by ignoring nodes already visited'''
        cost = {}
        prev = {}
        explored = {}
        # Dictionary initialization
        for i in range(map_.width):
            for j in range(map_.length):
                cost[str(i) + ',' + str(j)] = math.inf
                prev[str(i) + ',' + str(j)] = None
                explored[str(i) + ',' + str(j)] = False
        current_point = deepcopy(map_.start)
        current_point.comparator = 0

        cost[str(current_point.x) + ',' + str(current_point.y)] = 0

        # Add start node to the queue
        q.put(current_point)
        # Search loop
        while q.qsize() > 0:
            # Get new point from PQ
            v = q.get()
            if explored[str(v.x) + ',' + str(v.y)]:
                continue
            explored[str(v.x) + ',' + str(v.y)] = True
            # Check if popping off goal
            if v.x == map_.getEndPoint().x and v.y == map_.getEndPoint().y:
                break

            # Evaluate neighbors
            neighbors = map_.getNeighbors(v)
            for neighbor in neighbors:
                # alt = map_.getCost(v, neighbor) + cost[str(v.x)+','+str(v.y)]
                # 加入heuristic
                alt = map_.getCost(v, neighbor) + cost[str(v.x) + ',' + str(v.y)]
                if alt < cost[str(neighbor.x) + ',' + str(neighbor.y)]:
                    cost[str(neighbor.x) + ',' + str(neighbor.y)] = alt
                    neighbor.comparator = alt + heuristic(neighbor, map_.getEndPoint(), map_)
                    prev[str(neighbor.x) + ',' + str(neighbor.y)] = v
                q.put(neighbor)

        # Find and return path
        path = []
        while not (v.x == map_.getStartPoint().x and v.y == map_.getStartPoint().y):
            path.append(v)
            v = prev[str(v.x) + ',' + str(v.y)]
        path.append(map_.getStartPoint())
        path.reverse()
        return path


class AStarMSH(AIModule):

    def createPath(self, map_):
        q = PriorityQueue()
        ''' Maintain three dictionaries to keep track of cost ("x,y" -> cost per
        node), previous (node -> parent). This keeps track of paths, and explored
        which helps us run faster by ignoring nodes already visited'''
        cost = {}
        prev = {}
        explored = {}
        # Dictionary initialization
        for i in range(map_.width):
            for j in range(map_.length):
                cost[str(i) + ',' + str(j)] = math.inf
                prev[str(i) + ',' + str(j)] = None
                explored[str(i) + ',' + str(j)] = False
        current_point = deepcopy(map_.start)
        current_point.comparator = 0

        cost[str(current_point.x) + ',' + str(current_point.y)] = 0

        # Add start node to the queue
        q.put(current_point)
        # Search loop
        while q.qsize() > 0:
            # Get new point from PQ
            v = q.get()
            if explored[str(v.x) + ',' + str(v.y)]:
                continue
            explored[str(v.x) + ',' + str(v.y)] = True
            # Check if popping off goal
            if v.x == map_.getEndPoint().x and v.y == map_.getEndPoint().y:
                break

            # Evaluate neighbors
            neighbors = map_.getNeighbors(v)
            for neighbor in neighbors:
                # alt = map_.getCost(v, neighbor) + cost[str(v.x)+','+str(v.y)]
                # 加入heuristic
                alt = map_.getCost(v, neighbor) + cost[str(v.x) + ',' + str(v.y)]

                #
                if alt < cost[str(neighbor.x) + ',' + str(neighbor.y)]:
                    cost[str(neighbor.x) + ',' + str(neighbor.y)] = alt
                    neighbor.comparator = alt + 1.05 * heuristic(neighbor, map_.getEndPoint(), map_)
                    prev[str(neighbor.x) + ',' + str(neighbor.y)] = v

                q.put(neighbor)

        # Find and return path
        path = []
        while not (v.x == map_.getStartPoint().x and v.y == map_.getStartPoint().y):
            path.append(v)
            v = prev[str(v.x) + ',' + str(v.y)]
        path.append(map_.getStartPoint())
        path.reverse()
        return path
