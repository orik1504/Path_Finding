from turtle import xcor
import pygame 
from board import Grid
from board import Node
import math

class Gui_board(Grid):
    """ This class will create a board that the user will interact with
     will place blocking pathes, start point and end point

        0 - white -> blank cell 
        1 - black -> border/ blocking path
        2 - green -> open neighbors
        3 - red -> closed neighbors
        4 - orange -> end point
        5 - blue -> start point
        6 - purple -> the shortest path
    """
    colors = {"white":(255,255,255), "black":(0,0,0), "green":(0,128,0), "red":(255,0,0), "orange":(255, 165, 0), "blue":(0,255,255), "purple":(128,0,128), "gray":(128,128,128)}

    def __init__(self,size,width):
        """ This functuion will start a new clean grid """
        super().__init__(size,width)
        self.window = pygame.display.set_mode((self.width, self.width))

    def change_bg_to_white(self,):
        self.window.fill((self.colors["white"]))
        pygame.display.update()
    
    def draw_node(self,node,color):
        node.change_color(self.colors[color])
        pygame.draw.rect(self.window, node.color, (node.x*node.width, node.y*node.width, node.width, node.width))
        self.create_grid_lines()
        pygame.display.update()
    
    def get_clicked_location(self, pos): #* a function to get the top right corner of each node, this represents the node location
        x, y = pos
        return x//self.node_gap, y// self.node_gap #* I will get the x,y locations of the certain node

    def create_grid_lines(self,):
        GRAY = (128,128,128)
        for row in range(self.size):
            pygame.draw.line(self.window,GRAY,(0,row*self.node_gap),(self.width,row*self.node_gap))
            for col in range(self.size):
                pygame.draw.line(self.window,GRAY,(col*self.node_gap,0),(col*self.node_gap,self.width))
        pygame.display.update()
    
    def check_if_one_node(self,is_starting:bool):
        for row in range(self.size):
            for col in range(self.size):
                if is_starting:
                    if self.grid[row][col].color == self.colors["blue"]:
                        return False
                else:
                    if self.grid[row][col].color == self.colors["orange"]:
                        return False
        return True



def main():
    run  = True
    board = Gui_board(20,1000)
    board.change_bg_to_white()
    board.create_grid_lines()
    print(board.grid)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #TODO: need to check if I have only one start point and one end point
            mouse_click = pygame.mouse.get_pressed(5)
            if mouse_click: 
                x,y = board.get_clicked_location(pygame.mouse.get_pos())
                node = board.grid[x][y]
                if mouse_click[0]: # * Left click on mouse, will represent barrier 
                    board.draw_node(node,"black")

                if mouse_click[2]: # * right click on mouse, will represent clean 
                    board.draw_node(node,"white")

                if node.is_empty():    
                    if mouse_click[4] and board.check_if_one_node(True): # * far side mouse click , will represent the start point
                        board.draw_node(node,"blue")

                    if mouse_click[3] and board.check_if_one_node(False): # * close side mouse click, will represent the end point
                        board.draw_node(node,"orange")




    
pygame.quit()


if __name__ == "__main__":
    main()





        