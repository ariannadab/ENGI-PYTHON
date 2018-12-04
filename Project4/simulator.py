import random
import math
from matplotlib import pyplot as plt
import numpy as np

def image_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red,green,blue = range(3)
    # img array 
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    img = np.zeros((150,150,3))
    for x in range(50):
        for y in range(50):
            # red pixels
            img[x,y,red] = 1.0
            # purple pixels
            # set 3 color components 
            img[x+50, y+50,:] = (.5,.0,.5)
            # green pixels
            img[x+100,y+100,green] = 1.0
    plt.imshow(img)

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.6    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.step=0
        
    def infect(self):
        self.state = "I"
        self.step+=1
        
    def recover(self):
        self.state = "S"
        self.steps=0
        
    def die(self):
        self.state="R"
        
    def process(self, adjacent_cells):
        if self.state=="I":
            if self.step==recovery_time:
                self.recover()
            elif random.random()<=pdeath(self.step,4,1):
                self.die
            else:
                self.step+=1
                for cell in adjacent_cells:
                    if cell.get_state()=="S" and random.random()<=virality:
                        cell.infect()
                        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_state(self):
        return self.state
    
    def get_step(self):
        return self.step
    
    def __str__(self):
        return str(self.x)+" "+str(self.y)+" "+self.state
        
        
class Map(object):
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cells[(cell.get_x(),cell.get_y())] = cell
        
    def display(self):
        image = [[(0.0,0.0,0.0) for i in range(self.width)] for j in range(self.height)]
        for (key, cell) in self.cells.items():
            state = cell.get_state()
            if state == "S":
                image[cell.get_x()][cell.get_y()] = (0.0,1.0,0.0)
            elif state == "R":
                image[cell.get_x()][cell.get_y()] = (0.5, 0.5, 0.5) 
            else:
                image[cell.get_x()][cell.get_y()] = (1.0, 0.0, 0.0) 
        plt.imshow(image)
    
    def adjacent_cells(self, x,y):
        adj_cells = []
        if x > 0:
            if (x - 1,y) in self.cells:
                adj_cells.append(self.cells[(x - 1,y)])
        if x < self.width - 1:
            if (x + 1,y) in self.cells:
                adj_cells.append(self.cells[(x + 1,y)])
        if y > 0:
            if (x,y - 1) in self.cells:
                adj_cells.append(self.cells[(x,y - 1)])
        if y < self.height - 1:
            if (x,y + 1) in self.cells:
                adj_cells.append(self.cells[(x,y + 1)])
        return adj_cells
    
    def time_step(self):
        for (key, cell) in self.cells.items():
            cell.process(self.adjacent_cells(cell.get_x(), cell.get_y()))        
        self.display()

            
def read_map(filename):
    
    m = Map()
    
    nyc_map = open(filename,'r')
    for line in nyc_map:
        coord = line.strip().split(",")
        cell = Cell(int(coord[0]),int(coord[1]))
        m.add_cell(cell)
    
    return m
