import cv2 as cv
import numpy as np
from queue import PriorityQueue
import matplotlib.pyplot as plt
import time
import pygame as pyg


def createMap():
    map = []

    plt.xlim([0,601])
    plt.ylim([0,251])

    # Starting clearance for wall
    for x in range(0,601):
        for y in range(0,6):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='clearance')

    for x in range(0,601):
        for y in range(245,251):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='clearance')

    for x in range(0,6):
        for y in range(0,251):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='clearance')

    for x in range(595,601):
        for y in range(0,251):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='clearance')
    # Ending clearance for wall
    
    # Rectangle
    # Side 1
    for x in range(100,151):
        for y in range(0,101):
            map.append((x,y))
            plt.scatter(x,y, c= "green", label='Map-rectangle')

    # Clearance
    for x in range(95,100):
        for y in range(0,101):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')
        for y in range(145,151):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')

    """ for x in range(95,100):
        for y in range(145,151):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle') """
    
    for x in range(100,151):
        for y in range(101,106):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')
        for y in range(145,151):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')

    """ for x in range(100,151):
        for y in range(145,151):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle') """
    
    for x in range(151,156):
        for y in range(0,106):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')
        for y in range(145,151):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')
    
    
    for x in range(100,151):
        for y in range(150,251):
            map.append((x,y))
            plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(95,100):
        for y in range(150,251):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')

    for x in range(95,100):
        for y in range(100,105):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')
    
    for x in range(100,151):
        for y in range(101,105):
            map.append((x,y))
            plt.scatter(x,y, c= "blue", label='Map-rectangle')
    
    # Dhanush
    for x in range(460,601):
        for y in range(25,121):
            if 2*x - y <= 895:
                map.append((x,y))
                plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(460,511):
        for y in range(125,226):
            if 2*x+y <= 1145:
                map.append((x,y))
                plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(235,366):
        for y in range(85,161):
            map.append((x,y))
            plt.scatter(x,y, c= "green", label='Map-rectangle')

    # guru 
    for x in range(235,301):
        for y in range(160,199):
            if 38*x - 65*y >= -1470:
                map.append((x,y))
                plt.scatter(x,y, c= "green", label='Map-rectangle')
    
    for x in range(300,366):
        for y in range(160,199):
            if 38*x + 65*y <= 24270:
                map.append((x,y))
                plt.scatter(x,y, c= "green", label='Map-rectangle')

    for x in range(300,366):
        for y in range(58,86):
            if 27*x - 65*y <= 4330:
                map.append((x,y))
                plt.scatter(x,y, c= "green", label='Map-rectangle')

    for x in range(235,301):
        for y in range(58,86):
            if 27*x + 65*y >= 11870:
                map.append((x,y))
                plt.scatter(x,y, c= "green", label='Map-rectangle')
        
    plt.show()
    return map

def flip_coordinates(coordinates, ht):
    # Used to convert the coordinates to pygame coordinates (bottom left => top left)
    return (coordinates[0], ht - coordinates[1])

def flip_rectangle_coords(coords, height, obj_height):
    """Convert an object's coords into pygame coordinates (lower-left of object => top left in pygame coords)."""
    return (coords[0], height - coords[1] - obj_height)

def game(closed_list, backtrack_nodes):
    pyg.init()
    display_plot = pyg.display.set_mode((600,250))
    condn = False
    clk = pyg.time.Clock()


    clearance_rect_down = flip_rectangle_coords([95, 0], 250, 105)
    clearance_rect_up = flip_rectangle_coords([95, 145], 250, 105)

    clearance_triangle_1 = flip_coordinates([455, 20], 250)
    clearance_triangle_2 = flip_coordinates([463, 20], 250)
    clearance_triangle_3 = flip_coordinates([515.5, 125], 250)
    clearance_triangle_4 = flip_coordinates([463, 230], 250)
    clearance_triangle_5 = flip_coordinates([455, 230], 250)

    clearance_hexagon_1 = flip_coordinates([300, 205.76], 250)
    clearance_hexagon_2 = flip_coordinates([230, 165.38], 250)
    clearance_hexagon_3 = flip_coordinates([230, 84.61], 250)
    clearance_hexagon_4 = flip_coordinates([300, 44.23], 250)
    clearance_hexagon_5 = flip_coordinates([370, 84.61], 250)
    clearance_hexagon_6 = flip_coordinates([370, 165.38], 250)

    while not condn:
        for frame in pyg.event.get():
            if frame.type == pyg.QUIT:
                condn = True

        pyg.draw.rect(display_plot, (0,0,255), pyg.Rect(clearance_rect_down[0], clearance_rect_down[1], 60, 105))
        pyg.draw.rect(display_plot, (0,0,255), pyg.Rect(clearance_rect_up[0], clearance_rect_up[1], 60, 105))
        pyg.draw.polygon(display_plot, (0,0,255), ((clearance_hexagon_1),(clearance_hexagon_2),(clearance_hexagon_3),(clearance_hexagon_4),(clearance_hexagon_5),(clearance_hexagon_6)))
        pyg.draw.polygon(display_plot, (0,0,255), ((clearance_triangle_1),(clearance_triangle_2),(clearance_triangle_3), (clearance_triangle_4), (clearance_triangle_5)))

        pyg.draw.rect(display_plot, (255,0,0), pyg.Rect(100, 0, 50, 100))
        pyg.draw.rect(display_plot, (255,0,0), pyg.Rect(100, 150, 50, 100))
        pyg.draw.polygon(display_plot, (255,0,0), ((235,87.5),(300,50),(365,87.5),(365,162.5),(300,200),(235,162.5)))
        pyg.draw.polygon(display_plot, (255,0,0), ((460, 25),(460, 225),(510, 125)))
        
        ## Wall definition
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(0, 0, 5, 250))
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(595, 0, 5, 250))
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(0, 0, 600, 5))
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(0, 245, 600, 5))

        for val in closed_list:
            pyg.draw.circle(display_plot, "purple", flip_coordinates(val, 250), 1)
            pyg.display.flip()
            clk.tick(500)

        for item in backtrack_nodes:
            pyg.draw.circle(display_plot, "gray", flip_coordinates(item, 250), 1)
            pyg.display.flip()
            clk.tick(30)
        pyg.display.flip()
        pyg.time.wait(3000)
        condn = True
    pyg.quit()


def back_tracking(path, initial_state, current_node):
    optimal_path = []
    """ initial_state = initial_state
    current_node = current_node """
    optimal_path.append(current_node)
    parent_path = current_node
    while parent_path != initial_state:  
        parent_path = path[parent_path]
        optimal_path.append(parent_path)
    
    optimal_path.reverse()
    return optimal_path, len(optimal_path)

def check_duplicate(Node, prev_coordinates):
    for i in range(p_q.qsize()):
        if p_q.queue[i][1] == Node[1]:
            print("co-ordinate already existing")
            if p_q.queue[i][0] > Node[0]:
                p_q.queue[i] = Node
                return
            else:
                return
    
    p_q.put(Node)
    node_path[Node[1]] = prev_coordinates 
                     

def ActionMoveLeft(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr-1, y_curr)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr)) 


def ActionMoveRight(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr+1, y_curr)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr))

def ActionMoveUp(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr, y_curr+1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr))

def ActionMoveDown(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr, y_curr-1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr))

def ActionMoveUpLeft(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr-1, y_curr+1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr))

def ActionMoveUpRight(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr+1, y_curr+1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr))

def ActionMoveDownLeft(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr-1, y_curr-1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr))

def ActionMoveDownRight(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr+1, y_curr-1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr))

p_q = PriorityQueue()

obstacleMap = createMap()
#print(obstacleMap)


sourceNode_status = False
goalNode_status = False
source_point = ()
goal_point = ()

while sourceNode_status == False:

    print("Enter the x and y co-ordinate of source node in integer : ")
    x_source = int(input()) 
    y_source = int(input())
    source_point = (x_source,y_source)
    print("The source node is :")
    print(source_point)

    if source_point not in obstacleMap:
        sourceNode_status = True
        print("The entered source node co-ordinate is not an obstacle. ")
        break

    else:
        print("The entered source node co-ordinate is an obstacle. Please enter another co-ordinate ")

while goalNode_status == False:

    print("Enter the x and y co-ordinate of goal node in integer : ")
    x_goal = int(input()) 
    y_goal = int(input())
    goal_point = (x_goal,y_goal)

    if goal_point not in obstacleMap:
        goalNode_status = True
        print("The entered goal node co-ordinate is not an obstacle. ")
        break

    else:
        print("The entered goal node co-ordinate is an obstacle. Please enter another co-ordinate ")

visited_nodes = []
node_path = {}
source_node = (0,source_point)
status = False
p_q.put(source_node)
start = time.time()
while True:
    curr_node = p_q.get()
    visited_nodes.append(curr_node[1])
    (x,y) = curr_node[1]
    #visited_nodes.append(curr_node)
    if curr_node[1] != goal_point:
        if y-1 > 0:
            ActionMoveDown(curr_node, obstacleMap)
        if x-1 > 0:
            ActionMoveLeft(curr_node, obstacleMap)
        if y+1 < 250:
            ActionMoveUp(curr_node, obstacleMap)
        if x+1 < 600:
            ActionMoveRight(curr_node, obstacleMap)
        if x-1 > 0 and y+1 < 250:
            ActionMoveUpLeft(curr_node, obstacleMap)
        if x+1 < 600 and y+1 < 250:
            ActionMoveUpRight(curr_node, obstacleMap)
        if x-1 > 0 and y-1 > 0:
            ActionMoveDownLeft(curr_node, obstacleMap)
        if x+1 < 600 and y-1 > 0:
            ActionMoveDownRight(curr_node, obstacleMap)
        
    else:
        end = time.time()
        time_taken = end-start
        print("Reached")
        print("Reached x coordinate is:",x)
        print("Reached y coordinate is:",y)
        print("time taken for reaching from source to destination is ", time_taken)
        backtracking_data, length = back_tracking(node_path, source_point, curr_node[1])
        print(backtracking_data)
        break

game(visited_nodes, backtracking_data)








