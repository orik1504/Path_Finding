class Node():
    """ A class that will make a Node on the board"""

    def __init__(self, x:int, y:int, width:int, color):
        """ Every node on the grid will start blank (which in this case white) that will be represented by a certain number
        0 - white -> blank cell (255,255,255)
        1 - black -> border/ blocking path (0,0,0)
        2 - green -> open neighbors (0,128,0)
        3 - red -> closed neighbors (255,0,0)
        4 - orange -> end point (255, 165, 0)
        5 - blue -> start point (0,0,255)
        6 - purple -> the shortest path (128,0,128)
        7 - gray -> grid lines (128,128,128)
        """

        self.x = x # ! We will get that from 'Grid' class, it will return for us the x and y positions of the certain node 
        self.y = y # ! We will get that from 'Grid' class, it will return for us the x and y positions of the certain node
        self.width = width # * the node width (will make a square with width X width dimensions)
        self.color = color # * at first the node color will be white/blank
        self.neighbors = [] # * the neighbors of certain node, will be the other nodes that seround the current node

    def update_neighbors(self):
        """ will update the neighbors of current node """
        # * the neighbors are node instances but changing the node.x and node.y by 1 every time.
        pass
    
    def change_color(self,color):
        self.color = color
    
    def is_empty(self):
        return self.color == (255,255,255) or self.color == None
    
    def __lt__(self,other):
        return False


    

class Grid(Node):
    """ Will make a board (list of listst) using the node class in each index """
    def __init__(self, size:int , width):
        self.size = size # * size might refer to rows
        self.width = width
        self.node_gap = width//size
        self.grid = list()
        self.create_grid()

    
    def create_grid(self):
        """ this function will make nested list of nodes, that will be size X size grid
        for example - grid with size = 3:
            [[Node(x1,y1,gap),Node(x2,y2,gap),Node(x3,y3,gap)],
             [Node(x4,y4,gap),Node(x5,y5,gap),Node(x6,y6,gap)],
             [Node(x7,y7,gap),Node(x8,y8,gap),Node(x9,y9,gap)]] """
        for row in range(self.size):
            node_gap = self.width//self.size
            self.grid.append([Node(row,col,self.node_gap,None) for col in range(self.size)])

    
    def get_distance(self,node1, node2):
        return self.width*(abs(node1.x-node2.x)+abs(node1.y-node2.y))
   
