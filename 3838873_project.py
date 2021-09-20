
"""
    * * * [Note] * * *

    ** Run this code using the Python IDLE environment, do not 
    ** use Spyder (Anaconda) as it does simulate the path of the object in real time.
    ** The python IDLE environment (python command prompt) displays the object/motion in real time.

"""

# Xola Kota
# 3838873
# Computational Physics 322
# project


""" 
    This python code simulates a projectile under the influence of gravitation acceleration. 
    The simulation uses physics equations of motion(classical physics) which will help simulate
    the objects motion according to given variables such as the acceleration, 
    initial velocity and other physics variables that affect an objects motion. 
    It is a graphical simulation showing the path of an object in time.   

"""

# The imports below are important to requirements for the code

import math
from math import cos, sin, radians
import numpy as np
import matplotlib.pyplot as plt

# Program starter
print(" * * * Hello there !!! * * * ")
print(" * * * Projectile Simulator * * *")
print("")

# if the action variable == "n" run the code again
# if the user enters "y" when asked to exit the program then
# the action variable is changed to action = "y" and the code exits 
action = "n"
while action == "n":
    # Ask for physics variables to simulate the projectile
    # Vo = initial velocity
    # angle = in degrees
    # g = gravitational acceleration 
    
    g = float(input("Enter gravitational acceleration experienced by the object in m/s^2: "))
    angle = float(input("Enter the initial angle in degrees at which the object is thrown: "))
    Vo = float(input("Enter the initial velocity of the object in m/s: "))
    
    # Degrees are converted to radians
    # Total time = 2Vo*sin(angle)/g
    # Max height = Vo^2*sin^2(angle)/(2g)
    # R = Vo^2*sin(2*angle)/g

    total_time_1 = 2*Vo*sin(radians(angle))/g                    
    max_height_1 = math.pow(Vo, 2)*math.pow(sin(radians(angle)), 2)/(2*g)        
    range_1 = math.pow(Vo, 2)*sin(radians(2*angle))/g                

    # Calculation the x and y components of Vo
    Vox = Vo*cos(radians(angle))
    Voy = Vo*sin(radians(angle))

    # Number of discretely plotted points before first bounce 
    steps_1 = 17

    # Array time_1 has time point values of the object before the first bounce on the ground 
    time_1 = np.linspace(0.0, total_time_1, steps_1)

    # For showing the path of the object
    plt.figure(1)
    plt.suptitle('The Projectile Simulation', fontweight='bold', fontsize='16')
    plt.grid()
    plt.xlabel("Horizontal Distance On The Ground (m)")
    plt.ylabel("Vertical Distance Above The Ground (m)")

    # Defining x and y values in real time, since this is a simulation  
    for t in time_1:
        # x value distance from starting point at time t = 0 to time t = total_time_1
        x_1 = Vox*t
        # y value distance from starting point at time t = 0 to time t = total_time_1
        y_1 = Voy*t - 0.5*g*np.power(t, 2)

        # Plotting x and y values in real time
        plt.plot([x_1], [y_1], 'bo', markersize=9)

        # Show time t at each object point on the path
        plt.annotate('%.2f s' % t, xy=(x_1, y_1), fontsize='9', horizontalalignment='center', verticalalignment='bottom')
        plt.pause(total_time_1/steps_1)

    # After first bounce

    # Value for coefficient of restitution e (at each bounce the objects Voy and Vox values decrease)
    e = 0.7

    # Number of discretely plotted points after first bounce 
    steps_2 = 13

    # Calculations for more object bounces
    for n in [1, 2, 3]:
        
        # After each bounce the Voy and Vox values decrease due to variable e
        Vox = Vox + (e-1)*Voy
        # The initial angle will remain constant at each bounce
        Voy = e*Voy

        # New Vo after bounce 
        Vo_1 = Voy/sin(radians(angle))

        # Recalculating total_time, max_height and range for new bounce
        total_time_2 = 2*Vo_1*sin(radians(angle))/g                                        
        max_height_2 = math.pow(Vo_1, 2)*math.pow(sin(radians(angle)), 2)/(2*g)            
        range_2 = math.pow(Vo_1, 2)*sin(radians(2*angle))/g                                

        # New time values for the new bounce
        time_2 = np.linspace(0.0, total_time_2, steps_2)

        # Similar calculatations for x and y values to the variable calculations made before the first bounce
        for t in time_2:
            x_1 = range_1 + Vox*t
            y_1 = Voy*t - 0.5*g*np.power(t, 2)
            #Plotting x and y values for new object bounces in real time 
            plt.plot([x_1], [y_1], 'ro', markersize=9)
            # Show time t at each object point on the path
            plt.annotate('%.2f s' % (t+total_time_1), xy=(x_1, y_1), fontsize='9', horizontalalignment='center', verticalalignment='bottom')
            
            plt.pause(total_time_2/steps_2)

        # Update steps ,total time and range in the x direction after each bounce
        steps_2 = steps_2 - 2
        range_1 = range_1 + range_2                
        total_time_1 = total_time_1 + total_time_2

    # Displaying simulation
    plt.show()

    action = str(input("Do you want to exit simulation ?, type 'n' for no and 'y' for yes: "))

print("Programm ended...")
