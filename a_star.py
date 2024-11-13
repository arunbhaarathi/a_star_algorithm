import pygame
import sys
from queue import PriorityQueue
import itertools

pygame.init()
WIN_SIZE=600
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
YELLOW=(255, 223, 0)
GRAY=(128, 128, 128)


screen=pygame.display.set_mode((WIN_SIZE,WIN_SIZE))
pygame.display.set_caption("A-STAR ALGORITHM")


class cell:
    def __init__(self, pos):
        self.position=pos #(row,col)
        self.g=float('inf')
        self.h=float('inf')
        self.parent=None
        self.color=WHITE

    def calcualte_h(self,goal):
        #manhattan distance
        self.h=abs(self.position[0]-goal.position[0])+abs(self.position[1]-goal.position[1])

    def get_neighbors(self, grid, rows):
        self.neighbors=[]
        # Define neighbors with boundary checks
        up = grid[self.position[0] - 1][self.position[1]] if self.position[0] - 1 >= 0 else None
        down = grid[self.position[0] + 1][self.position[1]] if self.position[0] + 1 < rows else None
        left = grid[self.position[0]][self.position[1] - 1] if self.position[1] - 1 >= 0 else None
        right = grid[self.position[0]][self.position[1] + 1] if self.position[1] + 1 < rows else None

        if up is not None and up.color != BLACK:
            self.neighbors.append(up)
        if down is not None and down.color != BLACK:
            self.neighbors.append(down)
        if left is not None and left.color != BLACK:
            self.neighbors.append(left)
        if right is not None and right.color != BLACK:
            self.neighbors.append(right)
        
        return self.neighbors

    
    def set_color(self,color):
        self.color=color

def create_grid(rows,cols,node_size):
    grid=[]
    # screen.fill((255,255,255))
    for row in range(rows):
        grid.append([])
        for col in range(cols):
            node=cell((row,col))
            grid[row].append(node)
    return grid

def draw_grid(rows,cols,grid,node_size):
    # screen.fill(WHITE)
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, grid[row][col].color,(col*node_size,row*node_size,node_size,node_size))
            pygame.draw.rect(screen, BLACK,(col*node_size,row*node_size,node_size,node_size),1)
            # pygame.display.flip()
    return

def visualize_search(row,col,node_size,color):
    pygame.draw.rect(screen, color,(col*node_size,row*node_size,node_size,node_size))
    pygame.draw.rect(screen, BLACK,(col*node_size,row*node_size,node_size,node_size),1)
    pygame.display.flip()

def reconstruct_path(start,goal):

    curr_node=goal
    while curr_node!=start:
        curr_node=curr_node.parent
        curr_node.set_color(BLUE)

def grid_reset(rows,cols,grid,start,goal):
    for row in range(rows):
        for col in range(cols):
            grid[row][col].color=WHITE
    start=None
    goal=None
    return start,goal
    



def astar(start,goal,grid,rows,node_size):

    open_list=PriorityQueue()
    open_list_tracker=set()
    counter=itertools.count()
    open_list.put((0,next(counter),start)) #counter to tie-break nodes with same priority
    open_list_tracker.add(start)
    start.g=0
    closed_list=set()

    while not open_list.empty():
        current_node=open_list.get()[2]
        open_list_tracker.remove(current_node)

        if current_node==goal:
            reconstruct_path(start,goal)
            return

        neighbors=current_node.get_neighbors(grid,rows)

        for node in neighbors:
            if node in closed_list:
                continue
            
            current_g=current_node.g+1
            if current_g<node.g:
                node.g=current_g
            node.calcualte_h(goal)
            if node not in open_list_tracker:
                f=node.g+node.h
                open_list.put((f,next(counter),node))
                open_list_tracker.add(node)
                node.color=YELLOW
                visualize_search(node.position[0],node.position[1],node_size,node.color)
                node.parent=current_node
        current_node.color=GRAY
        visualize_search(current_node.position[0],current_node.position[1],node_size,node.color)
        closed_list.add(current_node)
    print("No path found")
    return



def main(win_size,rows):
    node_size=win_size//rows
    grid = create_grid(rows,rows,node_size)
    start_node=None
    goal_node=None
    run=True

    while run:
        draw_grid(rows,rows,grid,node_size)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run =False

            if pygame.mouse.get_pressed()[0]:
                    x,y=pygame.mouse.get_pos()
                    row,col=y//node_size,x//node_size
                    selected_node=grid[row][col]
                    if selected_node !=goal_node and start_node is None:
                        start_node=selected_node
                        start_node.color=RED
                    elif goal_node is None:
                        goal_node=selected_node
                        goal_node.color=GREEN
                    elif selected_node!=start_node and selected_node!=goal_node:
                        selected_node.color=BLACK
            elif pygame.mouse.get_pressed()[2]:
                x,y=pygame.mouse.get_pos()
                row,col=y//node_size,x//node_size
                selected_node=grid[row][col]
                if selected_node==start_node:
                    start_node.color=WHITE
                    start_node=None
                elif selected_node==goal_node:
                    goal_node.color=WHITE
                    goal_node=None
                else:
                    selected_node.color=WHITE

        
            for row in range(rows):
                for col in range(rows):
                    color = grid[row][col].color
                    if color is None:
                        print(row,col)
                        sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    astar(start_node,goal_node,grid,rows,node_size)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_node,goal_node=grid_reset(rows,rows,grid,start_node,goal_node)

            pygame.display.flip()


    pygame.quit()

main(WIN_SIZE,50)


"""THings to add: 
    4) add docstrings
    5) crerate unittest
    """