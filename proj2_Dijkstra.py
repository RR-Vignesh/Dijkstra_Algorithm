import cv2 as cv
import numpy as np
from queue import PriorityQueue
import matplotlib.pyplot as plt


def createMap():
    map = []

    plt.xlim([0,600])
    plt.ylim([0,250])

    """ for x in range(0,600):
        for y in range(0,5):
            map.append((x,y))
            #plt.scatter(x,y, c= "white", label='clearance') """

    for x in range(100,151):
        for y in range(0,101):
            map.append((x,y))
            # plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(100,151):
        for y in range(150,251):
            map.append((x,y))
            # plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(460,601):
        for y in range(25,121):
            if 2*x - y <= 895:
                map.append((x,y))
                # plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(460,511):
        for y in range(125,226):
            if 2*x+y <= 1145:
                map.append((x,y))
                # plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(235,366):
        for y in range(85,161):
            map.append((x,y))
            # plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(235,301):
        for y in range(160,199):
            if 38*x - 65*y >= -1470:
                map.append((x,y))
                # plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(300,366):
        for y in range(160,199):
            if 38*x + 65*y <= 24270:
                map.append((x,y))
                # plt.scatter(x,y, c= "green", label='Map-rectangle')

    for x in range(300,366):
        for y in range(58,86):
            if 27*x - 65*y <= 4330:
                map.append((x,y))
                # plt.scatter(x,y, c= "green", label='Map-rectangle')

    for x in range(235,301):
        for y in range(58,86):
            if 27*x + 65*y >= 11870:
                map.append((x,y))
                # plt.scatter(x,y, c= "green", label='Map-rectangle')
        
    #plt.show()
    return map
    

def check(Node):
"""     for i in visited_nodes:
        if Node[1] == i[1]:
            print("co-ordinate already existing")
            if Node[0] > i[0]:
                break
            else:
                for val in visited_nodes:
                     """


def ActionMoveLeft(curr_node, obstacle_map):
    coord = ()
    new_coord  = curr_node[1]
    coord = (new_coord[0]-1, new_coord[1])
    print(coord)   
    print(type(coord)) 

    if coord not in visited_nodes[1] and coord not in obstacle_map:
        visited_nodes.append(coord)
        cost = curr_node[0]+1
        new_node = (cost, coord)
        #check(new_node)
        p_q.put(new_node)  

    parent_node = tuple(curr_node[1])
    child_node = tuple(coord)
    node_path[child_node] = parent_node
    
    if coord != goal_point:
        return False
    else:
        return True 


p_q = PriorityQueue()


obsctacleMap = createMap()
print(obsctacleMap)


sourceNode_status = False
goalNode_status = False
source_point = ()
goal_point = ()

while sourceNode_status == False:

    print("Enter the x and y co-ordinate of source node in integer : ")
    #for i in range(0,2):
    x_source = int(input()) 
    y_source = int(input())
    source_point = (x_source,y_source)
    print("The source node is :")
    print(source_point)

    if source_point not in obsctacleMap:
        sourceNode_status = True
        print("The entered source node co-ordinate is not an obtsacle. ")
        break

    else:
        print("The entered source node co-ordinate is an obtsacle. Please enter another co-ordinate ")

while goalNode_status == False:

    print("Enter the x and y co-ordinate of goal node in integer : ")
    x_goal = int(input()) 
    y_goal = int(input())
    goal_point = (x_goal,y_goal)

    if goal_point not in obsctacleMap:
        goalNode_status = True
        print("The entered goal node co-ordinate is not an obtsacle. ")
        break

    else:
        print("The entered goal node co-ordinate is an obtsacle. Please enter another co-ordinate ")


visited_nodes = []
node_path = {}
source_node = (0,source_point)
status = False
p_q.put(source_node)
while p_q.empty() == False:
    curr_node = p_q.get()
    #visited_nodes.append(curr_node[1])
    visited_nodes.append(curr_node)
    if curr_node[1] != goal_point:
        status = ActionMoveUpLeft(curr_node, obsctacleMap)
    if status==False:
        ActionMoveUpRight(curr_node, obsctacleMap)
    if curr_node[1] != goal_point:
        ActionMoveDownLeft(curr_node, obsctacleMap)
    if curr_node[1] != goal_point:
        ActionMoveDownRight(curr_node, obsctacleMap)
    if curr_node[1] != goal_point:
        ActionMoveLeft(curr_node, obsctacleMap)
    if curr_node[1] != goal_point:
        ActionMoveRight(curr_node, obsctacleMap)
    if curr_node[1] != goal_point:
        ActionMoveUp(curr_node, obsctacleMap)
    if curr_node[1] != goal_point:
        ActionMoveDown(curr_node, obsctacleMap)
        








