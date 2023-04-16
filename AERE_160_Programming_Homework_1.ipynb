{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## AerE 160 Homework: Plotting with matplotlib\n",
    "The purpose of this homework assignment is to help you remember what you learned about programming in Python earlier in the semester, review some physics and to develop skills in using Python to plot equations that will be useful in other classes. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Nick McCullough, Section 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Review of numpy, matplotlib, and pint\n",
    "Numpy and matplotlib are the Python packages for array-based numerical calculation and for plotting respectively. These need to be imported. To get interactive plots you also need to specify ```%matplotlib notebook``` if using Jupyter or type ```%matplotlib qt``` into the command window if using Spyder. \n",
    "\n",
    "When using the https://class-jupyterhub.iastate.edu hosted Jupyter you also need to make sure you are using the aere160-python3 kernel\n",
    "\n",
    "Numpy, matplotlib, and pint all need to be ```import```ed to make them accessible through the variables ```np```, ```pl```, and ```pint```. Using the pint units library also requires creating a unit registry ``ur``"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib notebook\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as pl\n",
    "import pint\n",
    "\n",
    "ur=pint.UnitRegistry()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Rocket problem definition\n",
    "Let us use as an example predicting the trajectory of a model rocket launched from the Earth's surface. In this case, unlike our previous laboratory the rocket altitude will not get so large that we need to consider the change in gravitational field (remember $F_{g}=Gm_{1}m_{2}/r^{2}$?). Instead we will treat gravity as -9.81 m/s$^{2}$ down. The rocket thrusts for 2.0 seconds and then follows a ballistic trajgectory. We will treat the Earth as flat. We will neglect air resistance and assume the rocket has fins that keep it pointing in the direction it is moving. \n",
    "\n",
    "Let us define ```theta``` as the launch angle from the horizontal, so cos(theta) is the horizontal component and sin(theta) is the vertical component. We will assume that the orientation of the rocket does not change from ```theta``` during the thrust. \n",
    "\n",
    "We will look at the horizontal and vertical components of motion separately. Here are the parameters of the problem:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "theta = 70*ur.degree\n",
    "t_thrust = 2.0*ur.s\n",
    "magnitude_thrust = 3 * ur.N\n",
    "m = .050*ur.kg  # mass of rocket\n",
    "g = 9.81*ur.m/ur.s**2 # acceleration due to gravity"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Following what we did in the rocket lab assignment, create a unit vector ```T_direction``` calculated from theta indicating the direction of the thrust (be aware you may be relying on the unit conversions of pint as np.cos() and np.sin() normally expect parameters in radians).\n",
    "\n",
    "Multiply that direction times the thrust magnitude to get the thrust vector ```T_vector```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "T_direction = np.array((np.cos(theta.to(ur.radian)).magnitude,np.sin(theta.to(ur.radian)).magnitude))\n",
    "T_vector = T_direction*magnitude_thrust"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Setting up a time base\n",
    "In preparation for plotting -- in this case functions of time -- we usually want a range of values to plot over the horizontal axis. Use ```np.linspace()``` (from lab 2) to create a variable ```t``` with a range of times (in seconds -- multiply by ```ur.s```) from zero to 25 seconds. We recommend perhaps 50 points. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "t = np.linspace(0,25,50)*ur.s"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### 4. Horizontal motion, t <= t_thrust\n",
    "In the horizontal axis the rocket starts at rest, first accelerates according to the x (horizontal) component of the thrust ```T_direction[0]```. Then it moves at a constant rate. \n",
    "\n",
    "Your kinematic equations from Physics for constant acceleration include\n",
    "$$ x=x_{0} + v_{0}t + (1/2)at^{2}$$\n",
    "and \n",
    "$$ v=v_{0} + at.$$\n",
    "You will need to consider two different segments: ```t <= t_thrust``` and ```t > t_thrust```\n",
    "\n",
    "First we will create a variable ```x``` with units of meters to store the horizontal position and initialize it to zero. It will have the same number of elements as ```t``` and store double precision floating point numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = np.zeros((t.shape[0]),dtype='d')*ur.m"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Implicitly we are going to consider each element of ```x``` to correspond to the same-numbered element of ```t```. \n",
    "\n",
    "For the first segment, ```t <= t_thrust```, $v_{0}=0$ and $x=(1/2)a_{x}t^{2}$ where $a_{x}$ comes from $F_{x}=ma_{x}$ and $F_{x}$ is the horizontal component of the thrust vector ```T_vector[0]```.\n",
    "\n",
    "Define the variable ```ax``` to store the horizontal acceleration.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = t <= t_thrust"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since ```x``` and ```t``` have the same length and the elements implicitly correspond, if we want to operate on a subset of the elements, so long as we extract the same subset from both the two subsets will interoperate. \n",
    "\n",
    "We can use square brackets and an ```if```-like condition to select a subset of the elements of ```x``` for assignment and a subset of the elements of ```t``` for calculation. In selecting the first segment, that condition can be ```[t <= t_thrust]```, so we can write the position in that time period as"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-7-b76a93399962>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-7-b76a93399962>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    if x > 0.5\u001b[0m\n\u001b[0m               ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "x[t <= t_thrust] = 0.5 * ax * (t[t <= t_thrust]**2.0)\n",
    "if x > 0.5 \n",
    "    then t = 25\n",
    "if x < 2.0\n",
    "    then t = 50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The bracket notation selects only those elements where \n",
    "# the condition is satisfied. \n",
    "# So we can compare the output from printing x[t <= t_thrust]\n",
    "# with printing the entire array x:\n",
    "print(\"x = %s\" % (str(x)))\n",
    "print(\"x[t <= t_thrust] = %s\" % (str(x[t <= t_thrust])))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Horizontal motion, t > t_thrust\n",
    "\n",
    "We also need to calculate horizontal position in the second segment (after engine burnout). \n",
    "\n",
    "For the second segment  ```[t > t_thrust]``` (when the engine is no longer firing) the horizontal acceleration is zero but the initial position and velocity would be the final position and velocity from the first segment. \n",
    "\n",
    "The final position from the first segment can be calculated from \n",
    "$ x_{1} = (1/2)a_{x}t_{thrust}^{2} $\n",
    "\n",
    "The final velocity from the first segment can be calculated from \n",
    "$$ v_{x,1} = v_{0} + a_{x}t_{thrust} $$ \n",
    "where $v_{0}=0$ m/s for the first segment.\n",
    "\n",
    "Now calculate ```x1``` and ```vx1```. (Remember the power operator in Python is ```**```. If somehow you are using and old version of Python prior to version three then use 0.5 instead of 1/2) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x1 = t**2\n",
    "vx1 = 0 + (x+t)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate the horizontal positions in the second segment. \n",
    "At constant velocity our usual expression for position would be $x=x_{0} + v\\times(t-t_{0})$. In this segment the velocity is $v_{x,1}$, the initial position is $x_{1}$, and the starting time is $t_{thrust}$, so \n",
    "$$ x = x_{1} + v_{x,1}\\times(t-t_{thrust})  \\ \\ (\\mbox{ where } \\ \\ t > t_{thrust}) $$\n",
    "\n",
    "So evaluate position in the second segment. Remember to apply the ```[t > t_thrust]``` condition to ```t```:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x[t > t_thrust] = (t - t_thrust)*x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. Plotting horizontal position\n",
    "Now we can plot horizontal position as a function of time. \n",
    "\n",
    "When plotting with matplotlib you first need to create a figure with ```pl.figure()```. Then you can plot with ```pl.plot(x,y,'-')``` as we did in programming lab 2. When plotting the two parameters should be arrays of the same length with coordinates to be plotted on the horizontal and vertical axes respectively. The '-' is a format string that specifies how the data should appear on the plot. See https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html for a full list of format strings. \n",
    "\n",
    "It is good practice to explicitly convert the units to whatever you are going to print on the axis labels using the ```.to()``` method of the quantities.\n",
    "\n",
    "You can add horizontal and vertical axis labels with ```pl.xlabel()``` and ```pl.ylabel()```, and turn on a grid with ```pl.grid(True)```. \n",
    "\n",
    "If you made the plot interactive with ```%matplotlib notebook``` or ```%matplotlib qt``` you should be able to interactively zoom and manipulate it. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pl.figure()\n",
    "pl.plot(t.to(ur.s),x.to(ur.m),'-') # plot time on horizontal axis, horizontal position on vertical axis\n",
    "pl.xlabel('Time (s)')\n",
    "pl.ylabel('Horizontal position (m)')\n",
    "pl.grid(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7. Vertical motion, t <= t_thrust\n",
    "\n",
    "Vertical motion is similar to the horizontal motion except we have the presence of gravity as well. \n",
    "\n",
    "For the first segment, ```t <= t_thrust```, $v_{0}=0$ and $y=(1/2)a_{y}t^{2}$ where $a_{y}$ comes from $F_{y}=ma_{y}$ and $F_{y}$ is the vertical component of the thrust vector ```T_vector[1]``` minus the force of gravity $mg$.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 7a. LaTeX notation for equations. \n",
    "We need an expression for $a_{y}$. Translating the above words into an equation,\n",
    "$$ F_{y} = T_{vector,y} - mg = ma_{y}.$$\n",
    "\n",
    "One of the nice things about the Jupyter notebook is that it can display equations nicely using LaTeX notation (see https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html and https://en.wikibooks.org/wiki/LaTeX/Mathematics for more information). If you double click on this cell you can see how the above equation was entered, delineated with two dollars signs. The underscore _ means subscript and the {braces} group into that subscript. Equations on their own line use two dollars signs on each side, whereas inline expressions use a single dollars sign on each side. \n",
    "\n",
    "Solve this equation for $a_{y}$. Then double-click on the cell below to edit it and write the solution for $a_{y}$ using LaTeX notation. Pressing shift-enter or the \"Run\" button will create the nice-looking equation.  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$$ a_{y}= (put right hand side of equation here) $$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 7b. Back to calculating the vertical position in the first segment. \n",
    "\n",
    "Create a variable ```y``` with units of meters to store the vertical position and initialize it to zero. It should have the same number of elements as ```t``` and store double precision floating point numbers.\n",
    "\n",
    "Define the variable ```ay``` to store the horizontal acceleration\n",
    "and calculate its value based on your solution from above. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize y using np.zeros() as above\n",
    "y =\n",
    "\n",
    "# Calculate ay from your formula above. \n",
    "ay = "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As above, ```y``` and ```t``` have the same length and the elements implicitly correspond, so we can use square brackets to select identical subsets of the elements of ```y``` and  ```t``` for calculation. So we can write the position in the first segment as"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "y[t <= t_thrust] = <=t_thrust"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 8. Vertical motion, t > t_thrust\n",
    "\n",
    "We also need to calculate vertical position in the second segment (after engine burnout). \n",
    "\n",
    "For the second segment  ```[t > t_thrust]``` (when the engine is no longer firing) the vertical acceleration is just $-g$ but the initial position and velocity would be the final vertical position and velocity from the first segment. \n",
    "\n",
    "The final vertical position from the first segment can be calculated from \n",
    "$ y_{1} = (1/2)a_{y}t_{thrust}^{2} $\n",
    "\n",
    "The final velocity from the first segment can be calculated from \n",
    "$$ v_{y,1} = v_{0} + a_{y}t_{thrust} $$ \n",
    "where $v_{0}=0$ m/s for the first segment.\n",
    "\n",
    "Now calculate ```y1``` and ```vy1```, the initial position and velocity respectively for the second segment. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "y1 = \n",
    "vy1 = "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate the vertical positions in the second segment. \n",
    "Our expression for position would be $y=y_{1} + v_{y,1}(t-t_{thrust}) + (1/2)a_{y,2}(t-t_{thrust})^{2}$ based on initial position $y_{1}$, initial velocity $v_{y,1}$, acceleration $a_{y,2}$ and segment starting time $t_{thrust}$. The acceleration $a_{y,2}$ is just gravity (-g). \n",
    "\n",
    "So calculate the acceleration ```ay2``` then evaluate vertical (y) position in the second segment. Don't forget use use the brackets [t > t_thrust] to restrict the calculation to the subsets of ```y``` and ```t``` corresponding to times after thrust burnout."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ay2 = \n",
    "\n",
    "y[t > t_thrust] = "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 9. Plotting vertical position\n",
    "Now plot vertical position as a function of time. It should be nearly identical to the above\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pl.figure()\n",
    "# Create plot, set axis labels, etc. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 10. Plotting vertical and horizontal position as functions of time on the same plot.\n",
    "You can create a combined plot with multiple lines just by calling pl.plot() multiple times.\n",
    "You can add a legend to distinguish the lines with pl.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pl.figure()\n",
    "\n",
    "pl.plot() # Insert horizontal position call to pl.plot()\n",
    "\n",
    "pl.plot() # Insert vertical position call to pl.plot()\n",
    "\n",
    "# The pl.legend() call's first parameter is a tuple of label texts, \n",
    "# corresponding to the lines you have plotted\n",
    "# the \"loc=\" optional parameter allows you to specify where to put\n",
    "# the legend. \n",
    "pl.legend(('Horizontal position','Vertical position'),loc=\"best\")\n",
    "\n",
    "pl.xlabel('Time (s)')\n",
    "pl.ylabel('Position (m)')\n",
    "pl.grid(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 11. Visualizing the trajectory\n",
    "We can also make a plot of horizontal position against vertical position. In many cases you may want to illustrate positions in US conventional units instead of meters. So in this case, when converting the units with the ```.to()``` method, convert to ```ur.feet``` instead of ```ur.m``` (we have changed the axis labels appropriately).\n",
    "\n",
    "Also we will plot the point of engine burnout with an 'o' marker and label the trajectory appropriately.  Because we have not bounded our calculation when the rocket reaches the ground, our calculation keeps going until the time limit we set above.."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pl.figure()\n",
    "pl.plot() # plot x vs. y, converting to units of feet. \n",
    "\n",
    "pl.plot(x1.to(ur.feet),y1.to(ur.feet),'o') # plot location of engine burnout\n",
    "pl.legend(('Trajectory','Engine burnout location'),loc=\"best\")\n",
    "pl.xlabel('Horizontal position (feet)')\n",
    "pl.ylabel('Vertical position (feet)')\n",
    "pl.grid(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Saving/showing the figure\n",
    "\n",
    "You can save the figure as an image by clicking the disk icon on the figure, but \n",
    "the generated image may not be very high resolution. \n",
    "\n",
    "One useful trick is to programmatically save your figure\n",
    "with ```pl.savefig()``` as illustrated below.\n",
    "\n",
    "Another important tip: **When creating a plotting script for spyder you should always end it with pl.show()**. That way if you forget the ```%matplotlib qt``` or run it outside of spyder it will still bring up the figures. \n",
    "\n",
    "Congratulations on learning some of the basics of programming and plotting in Python, and on becoming a rocket scientist!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pl.savefig(\"my_rocket_trajectory.png\",dpi=300) # dpi parameter sets the image resolution"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Submission\n",
    "Submit the completed assignment to Canvas as a .html saved from Jupyter"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
