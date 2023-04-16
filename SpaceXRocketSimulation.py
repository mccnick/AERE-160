# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# You will need to paste the relevant code from above 
# into this template and run in Spyder. 
# Don't forget to type '%matplotlib qt'
# into the Spyder console before running to enable 
# the interactive plots
# 
# It should work in Jupyter notebook too but you 
# won't be able to detect keyboard input or mouse clicks
# to control the rocket. For it to work in Jupyter notebook, 
# you will need a '%matplotlib notebook' line at the top. 


# Template begins here
# --------------------

# Include import statements and unit registry from above
# (Remove the above line for Spyder; 
# you will need to type '%matplotlib qt' into the command window instead.)
import numpy as np
from matplotlib import pyplot as pl
import pint
ur = pint.UnitRegistry() # Import pint and create unit registry



# Include Rocket and planet characteristics; physics constants
empty_mass = 29500*ur.kg
payload = 1000*ur.kg
fuel_mass = 480000*ur.kg
tsfc = 3.5*(10**-4)*ur.s/ur.m
full_thrust = 7600*ur.kN
G = (6.674*(10**-11))*ur.m**3/(ur.kg*ur.s**2)
E = 5.98*(10**24)*ur.kg


# Include earth diameter, surface speed, initial rocket position,
# initial rocket velocity
# Earth's diameter is given by
d_earth = 12.7e6*ur.m 
# and Earth's tangential speed (due to rotation) is 
# approximately
v_surface = 460.0*ur.m/ur.s # at the equator
# Position vector
# This puts the horizontal (x) position at zero
# and the vertical (y) position at one earth radius
# (will be the initial position of our rocket)
pos = np.array((0.0,d_earth.to(ur.m).magnitude/2.0))*ur.m
# Define initial thrust angle and direction
vel = np.array((v_surface.to(ur.m/ur.s).magnitude,0.0))*(ur.m/ur.s)
# Given, for example
T_angle = 60.0*ur.degree # 60 deg. CCW from horizontal

# Evaluate and store T_direc. 
# The components of T_direc are the sine and cosine of T_angle
# (but you have to figure out which is which and whether there
# are any minus signs). Also the np.sin() and np.cos() functions
# take their parameters in radians, not degrees. 

# +x should be to the right and +y should be up. Make sure the 
# direction vector makes sense. 

# T_direction =
T_direction = np.array((np.cos(T_angle.to(ur.radian)).magnitude,np.sin(T_angle.to(ur.radian)).magnitude))


# Include code for the baseline plot and initial arrow
pl.ion() # interactive mode ON
fig = pl.figure()
pl.axis((-1e6,1e6,6e6,7e6)) # Define axis bounds in (assumed) meters
pl.grid(True) # Enable grid

# create green filled circle representing earth
earth = pl.Circle((0,0),float(d_earth/2.0/ur.m),color='g')
fig.gca().add_artist(earth)

# Add your Arrow-drawing code here
arrowplt = pl.arrow((pos[0].magnitude),pos[1].magnitude,((T_direction[0])*500000),((T_direction[1])*500000),width=300000)
fig.gca().add_artist(arrowplt)


# Include the event handler
def event_handler(event):
    global T_angle
    if event.key==',': # press comma to rotate left
        # Rotate left (increase angle)
        T_angle += 10.0*ur.degree
        pass
    elif event.key=='.': # press period to rotate right
        # Rotate right (decrease angle)
        T_angle -= 10.0*ur.degree
        pass
    elif hasattr(event,"button") and event.button==1:
        if event.xdata < 0.0: 
            # Click on left-half of plot to
            # Rotate left (increase angle)
            T_angle += 10.0*ur.degree
            pass
        else:
            # Click on right-half of plot to
            # Rotate right (decrease angle)
            T_angle -= 10.0*ur.degree
            pass
        pass
    
    pass

# Connect this event handler to the figure so it is called
# when the mouse is clicked or keys are pressed. 
fig.canvas.mpl_connect('key_press_event',event_handler)
fig.canvas.mpl_connect('button_press_event',event_handler)



# Include the vector norm function from the 
# force of gravity calculation, above. 
pl.axis((-1e6,1e6,6e6,7e6)) # Define axis bounds in (assumed) meters
# In the last lab we used np.linalg.norm() to find the magnitude of a vector.
# Unfortunately that function does not work with quantities that have units. 
# Instead, use this function norm() that does work with quantities that have units
def norm(vec):
    """Unit aware vector norm (magnitude)"""
    return np.sqrt(np.sum(vec**2.0))


# r =  # Should have units of distance (meters)
total_mass = empty_mass+fuel_mass+payload
Fg = (G*(empty_mass+fuel_mass+payload)*E)/norm(pos)**2
Direc_Gravity = -pos/norm(pos)
Vec_Gravity = Fg*Direc_Gravity


t=0.0 * ur.s # Start at t=0

# Loop until ctrl-C or press stop button on 
# Spyder console or t exceeds 36000 seconds (10 hours
# of simulated time)

while t < 36000 * ur.s: 
    # Select the time step (code above)
    if fuel_mass > 0:
        dt = 1*ur.s
    elif fuel_mass == 0:
        dt = 10*ur.s
        
    # Update the plot:     
    #  * Call arrowplt.remove() method on the old arrow
    arrowplt.remove()

    #  * Calculate the thrust (rocket) direction from
    #    the rocket angle (code way above)
    T_direction = np.array((np.cos(T_angle.to(ur.radian)).magnitude,np.sin(T_angle.to(ur.radian)).magnitude))

    #  * Plot the new arrow (code way above)    
    arrowplt = pl.arrow((pos[0].magnitude),pos[1].magnitude,((T_direction[0])*500000),((T_direction[1])*500000),width=300000)

    #  * Label the fuel state in the plot title, e.g.
    #    pl.title("Fuel remaining %f kg" % ())
    pl.title("Fuel remaining %f kg" % (fuel_mass.magnitude))

    #  * Show the time in the x axis label, e.g.
    #    pl.xlabel("Time = %f s" % ())
    pl.xlabel("Time = %f s" % (t.magnitude)) 

    #  * Select the plot region according to fuel state (code above)
    if fuel_mass > 0:
        pl.axis((-1e6,1e6,6e6,7e6))
    else:
        pl.axis((-1.1e7,1.1e7,-6e6,8.7e6))
    
    # These next two lines cause the plot display to refresh
    fig.canvas.draw()
    fig.canvas.flush_events()

    # Determine the forces on the rocket (code above): 
    total_mass = empty_mass+fuel_mass+payload
    Fg = (G*(empty_mass+fuel_mass+payload)*E)/norm(pos)**2
    Direc_Gravity = -pos/norm(pos)
    Vec_Gravity = Fg*Direc_Gravity

    #  * Calculate the magnitude of the force of gravity
    #  * Calculate the direction of the force of gravity
    #    and gravity vector on the rocket
    #  * Calculate the thrust vector
    if fuel_mass > 0*ur.kg:
        Tvec = T_direction*full_thrust
    else:
        Tvec = 0*ur.N*T_direction
    
    
    # Update the fuel mass (code above)
    if fuel_mass > 0:
        dm_f = (tsfc*-1*full_thrust)*dt
        fuel_mass = fuel_mass + dm_f
    if fuel_mass <= 0:
        fuel_mass = 0*ur.kg

    # Determine the change in velocity (code above)
    f=Tvec+Vec_Gravity
    a=f/(total_mass)
    dv=a*dt
    
    vel = vel+dv
    
    dpos = vel*dt

    # Determine the change in position (code above)
    pos = pos + dpos
    
    t = t + dt # Update the time
    pass  # End of loop block



