# Imports go at the top
from microbit import *

#Define Functions: forward, spinleft, spinright

def forward(time):
    #Move left motor forward at 50% power
    pin16.write_analog(770)
    pin8.write_analog(0)
    #Move right motor forward at 50% power
    pin14.write_analog(770)
    pin12.write_analog(0)
    #Wait for time (in seconds)
    sleep(time*1000)
    #Stop all motors
    pin16.write_analog(0)
    pin8.write_analog(0)
    pin14.write_analog(0)
    pin12.write_analog(0)
    sleep(500)

def spinleft(time):
    #Move left motor in reverse at 50% power
    pin16.write_analog(0)
    pin8.write_analog(770)
    #Move right motor forward at 50% power
    pin14.write_analog(770)
    pin12.write_analog(0)
    #Wait for time (in seconds)
    sleep(time*1000)
    #Stop all motors
    pin16.write_analog(0)
    pin8.write_analog(0)
    pin14.write_analog(0)
    pin12.write_analog(0)
    sleep(500)

def spinright(time):
    #Move left motor forward at 50% power
    pin16.write_analog(770)
    pin8.write_analog(0)
    #Move right motor forward at 50% power
    pin14.write_analog(0)
    pin12.write_analog(770)
    #Wait for time (in seconds)
    sleep(time*1000)
    #Stop all motors
    pin16.write_analog(0)
    pin8.write_analog(0)
    pin14.write_analog(0)
    pin12.write_analog(0)
    sleep(500)
    
#Test Code that runs when A button is pressed
while True:
   if button_a.is_pressed():
       sleep(2000)
       #Go forward for 0.5 seconds
       #forward(0.5)
       #Spin left for 0.5 seconds
       spinleft(0.5)
       #Spin right for 0.5 seconds
       spinright(0.5)
