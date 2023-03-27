
from matplotlib import pyplot as pl
import numpy as np

# Global variables
cur_pos_x = None
cur_pos_y = None
cur_direc = None
fig=None
started = False
arrowplt = None

def draw_arrow():
    global arrowplt
    
    arrow_len=30.
    arrow_width=5.
    
    if arrowplt is not None:
        arrowplt.remove()  # remove any preexisting arrow before we add a new one
        pass
    arrowplt = pl.arrow(cur_pos_x,cur_pos_y,arrow_len*np.cos(cur_direc),arrow_len*np.sin(cur_direc),width=arrow_width)

    
    # Set axis bounds on plot
    pl.axis((-200,200,-150,150))
    pl.grid(True)  # turn on grid
    
    pass
    
def start():
    global cur_pos_x,cur_pos_y,cur_direc,started,fig,arrowplt

    
    cur_pos_x = 0.0
    cur_pos_y = 0.0
    cur_direc = 0.0
    arrowplt = None
    started = True

    pl.ion() # interactive mode on
    
    fig=pl.figure() # Create figure window
    
    draw_arrow()

    # force immediate draw
    fig.canvas.draw()
    fig.canvas.flush_events()

    pass

def move(direction,distance):
    """ Move in the specified direction ("forward" or "back")
    by the given distance.
    """
    global cur_pos_x,cur_pos_y

    if not started:
        raise ValueError("Must call start() first!")
    
    if direction == "forward":
        # just use distance as given
        pass
    elif direction == "back":
        # negate distance
        distance = -distance
        pass
    else:
        raise ValueError("Direction not given as either \"forward\" or \"back\"")
        
    # Determine new position
    new_pos_x = cur_pos_x + distance*np.cos(cur_direc)
    new_pos_y = cur_pos_y + distance*np.sin(cur_direc)
    
    # Plot line from cur_pos to new_pos
    pl.plot((cur_pos_x,new_pos_x),(cur_pos_y,new_pos_y),'-',linewidth=3)
    
    # New position becomes new current position
    cur_pos_x = new_pos_x
    cur_pos_y = new_pos_y
    draw_arrow()
    # Force immediate draw
    fig.canvas.draw()
    fig.canvas.flush_events()
    pass

def turn(turndir,degrees):
    """Turn in the specified direction ("left" or "right") by the 
        given number of degrees"""
    global cur_direc
    if not started:
        raise ValueError("Must call start() first!")
    
    if turndir == "left":
        # Left turn adds to previous direction, converting degrees to radians
        cur_direc = cur_direc + degrees*np.pi/180  
        pass
    elif turndir == "right":
        cur_direc = cur_direc - degrees*np.pi/180 # Right turn subtracts from direction
        pass
    else:
        raise ValueError("Turn direction not given as either \"left\" or \"right\"")
    
    draw_arrow()
    # Force immediate draw
    fig.canvas.draw()
    fig.canvas.flush_events()
    pass

