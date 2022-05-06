#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 UltrasonicSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# List of objects that been Created here.

ev3 = EV3Brick()

back_wheels_motor = Motor(Port.A)
steering_motor = Motor(Port.D)

left_sensor = UltrasonicSensor(Port.S2)
right_sensor = UltrasonicSensor(Port.S3)
back_sensor = UltrasonicSensor(Port.S4)
color_senser = ColorSensor(Port.S1)




# In this part, I declared four different functions, each function related to each sensor

def traffic_light():
    '''
    This function related to color sensor.
    If the color sensor detects the red light at the front will return stop,
    otherwise it will returns Continue. 
    '''
    if color_senser.color() == Color.RED:

        return("STOP")
    else:
        return("Continue")

def object_on_left():
    '''
    This function related to left sensor.
    If the sensor detects no obstacle within 400mm range in front of the robot,
    this function returns OK, and it returns LNG otherwise. 
    '''
    if left_sensor.distance() >= 400:

        return("OK")
    else:
        return("LNG")

def object_on_right():
    '''
    This function related to right sensor.
    If the sensor detects no obstacle within 400mm range in front of the robot,
    this function returns OK, and it returns RNG otherwise. 
    '''
    if right_sensor.distance() >= 400:

        return("OK")
    else:
        return("RNG")

def object_on_back():
    '''
    This function related to back sensor.
    If the sensor detects no obstacle within 400mm range in front of the robot,
    this function returns OK, and it returns BNG otherwise. 
    '''
    if back_sensor.distance() >= 400:

        return("OK")
    else:
        return("BNG")


#In this part, I declard another four different functions, ecah function for driving in different direction.

def drive_forward():
    '''
    Go straight by rotating the back motors.
    '''
    back_wheels_motor.run_time(-400,2000)

def turn_right():
    '''
    First, this function turns the direction of steering to the right,
    then rotate the motor to make the car move to the right side. And finally,
    it changes the direction of the steering to the original setting.
    '''
    steering_motor.run_time(70,2000)
    back_wheels_motor.run_time(400,2000)
    steering_motor.run_time(-70,2000)
    
def turn_left():
    '''
    First, this function turns the direction of steering to the left,
    then rotate the motor and move to the left side. And finally,
    it changes the direction of the steering to the original position.
    '''
    steering_motor.run_time(-70,2000)
    back_wheels_motor.run_time(400,2000)
    steering_motor.run_time(70,2000)
    
def reverse():
    '''
    Go backward by rotating the wheel in the opposite direction.
    '''
    back_wheels_motor.run_time(400,2000)


# This part include the While loop, this While loop contains of seven different conditions.

while True:

    if traffic_light() == "Continue" and object_on_left() == "OK" and object_on_right() == "OK":
        ev3.screen.load_image(ImageFile.BACKWARD)
        drive_forward()
        
    elif traffic_light() == "STOP" and object_on_left() == "OK" and object_on_right() == "OK":
        back_wheels_motor.stop()
        ev3.screen.load_image(ImageFile.STOP_2)
        ev3.speaker.play_file(SoundFile.COLOR)
        ev3.speaker.play_file(SoundFile.RED)
        ev3.speaker.play_file(SoundFile.ONE)
        ev3.speaker.play_file(SoundFile.TWO)
        ev3.speaker.play_file(SoundFile.THREE)
        wait(1000) 
          
    elif traffic_light() == "Continue" and object_on_left() == "OK" and object_on_right() == "RNG" and object_on_back() == "OK":
        ev3.speaker.play_file(SoundFile.OBJECT)
        ev3.screen.load_image(ImageFile.RIGHT)
        ev3.speaker.play_file(SoundFile.TURN)
        ev3.speaker.play_file(SoundFile.LEFT)
        turn_left()
    
    elif traffic_light() == "Continue" and object_on_left() == "LNG" and object_on_right() == "OK" and object_on_back() == "OK":
        ev3.speaker.play_file(SoundFile.OBJECT)
        ev3.screen.load_image(ImageFile.LEFT)
        ev3.speaker.play_file(SoundFile.TURN)
        ev3.speaker.play_file(SoundFile.RIGHT)
        turn_right()

    elif traffic_light() == "STOP" and object_on_left() == "LNG" and object_on_right() == "RNG" and object_on_back() == "OK":
        ev3.screen.load_image(ImageFile.FORWARD)
        ev3.speaker.play_file(SoundFile.OBJECT)
        ev3.speaker.play_file(SoundFile.BACKWARDS)
        reverse()

    elif traffic_light() == "STOP" and object_on_left() == "LNG" and object_on_right() == "RNG" and object_on_back() == "BNG":
        back_wheels_motor.stop()
        ev3.screen.load_image(ImageFile.STOP_1)
        ev3.speaker.play_file(SoundFile.OBJECT)
        ev3.speaker.play_file(SoundFile.COLOR)
        ev3.speaker.play_file(SoundFile.RED)
        ev3.speaker.play_file(SoundFile.ONE)
        ev3.speaker.play_file(SoundFile.TWO)
        ev3.speaker.play_file(SoundFile.THREE)
        wait(1000)
    else:
        back_wheels_motor.stop()
        steering_motor.stop()
        back_wheels_motor.brake()
        steering_motor.brake()




