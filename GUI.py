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

