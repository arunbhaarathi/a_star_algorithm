import pygame
import sys

pygame.init()
WIN_SIZE=600
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

screen=pygame.display.set_mode((WIN_SIZE,WIN_SIZE))
pygame.display.set_caption("A-STAR ALGORITHM")


class cell:
    def __init__(self, pos):
        self.position=pos
        self.g=0
        self.h=0
        self.neighbors=[]
        self.parent=None
        self.visited=False
        self.color=WHITE
        self.is_obstacle=False

    def calcualte_h(self):
        pass

    def set_neighbors(self):
        pass
    
    def set_color(self,color):
        self.color=color

def create_grid(rows,cols,node_size):
    # grid=[[cell() for _ in range(cols)] for _ in range(rows)]
    grid=[]
    screen.fill((255,255,255))
    for row in range(rows):
        grid.append([])
        for col in range(cols):
            node=cell((row,col))
            grid[row].append(node)
            # pygame.draw.rect(screen, (0,0,0), (col * node_size, row * node_size, node_size, node_size), 1)

    return grid



def main(win_size,rows):
    node_size=win_size//rows


    grid = create_grid(rows,rows,node_size)

    start_node=None
    goal_node=None
    


    run=True

    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run =False

            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    x,y=pygame.mouse.get_pos()
                    row,col=y//node_size,x//node_size
                    selected_node=grid[row][col]
                    if selected_node !=goal_node and start_node is None:
                        start_node=selected_node
                        start_node.color=RED
                    elif goal_node is None:
                        goal_node=selected_node
                        goal_node.color=GREEN
                    else:
                        selected_node.color=BLACK
                elif event.button==3:
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

            # elif event.type==pygame.MOUSEBUTTONDOWN:
            #     if event.button==3:
            #         x,y=pygame.mouse.get_pos()
            #         row,col=y//node_size,x//node_size
            #         grid[row][col].visited=not grid[row][col].visited

        
            for row in range(rows):
                for col in range(rows):
                    color = grid[row][col].color
                    if color is None:
                        print(row,col)
                        sys.exit()
                    print((row,col,color))
                    pygame.draw.rect(screen,color,(col * node_size, row * node_size, node_size, node_size))
                    pygame.draw.rect(screen, (0,0,0), (col * node_size, row * node_size, node_size, node_size), 1)



            pygame.display.flip()


    pygame.quit()

main(WIN_SIZE,20)
