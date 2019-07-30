from wakeuper import Wakeuper
from Robotics import Robot_move
from servo import Servo
import time
from ultra import Ultra
import rospy, time
from geometry_msgs.msg import Point

keyboard_status = 0

def updateMagValue(msg):
    keyboard_status = msg.x

def keyboard_listener():
    rospy.init_node('text_listener')
    rospy.Substriber('vpollo', Point, updateMagValue)
    return keyboard_status
    #put it in a while loop at the end and read the inputs

def main():
    # main function
    # create instances
    wakeup = Wakeuper()
    roboMove = Robot_move()
    arms = Servo()
    #link the second ultrasonic sensor to 14, 15 channal and setup it
    isInBin = Ultra(14, 15)
    isInBin.setUp()

    # init substriber
    #rospy.Substriber('vpollo', Point, updateMagValue)
    #rospy.init_node('text_listener')


    while(True):
        while(not keyboard_listener() == 1]): pass

        roboMove.spin_and_detect('paperball')
        #after this, the robot should be ready to head towards obj
        #soooo, move straight to 
        roboMove.to_target('paperball')
        # annnnnd, stop
        roboMove.stop()
        #then, grab the ball
        # !!!!lack the grab func, may modify wait time!!!!
        arms.grab()

        # when grabbed, give it back to master
        roboMove.spin_and_detect('owner')
        roboMove.to_target('owner')
        roboMove.stop()
        # wait for 3 seconds for the owner to take the ball
        time.sleep(3.0)
        arms.let_go()
        

        #than head to homebase to wait for another throw
        roboMove.spin_and_detect('homebase')
        roboMove.to_target('homebase')
        roboMove.stop()

        while(True):
            if(isInBin.distance_to_spitball() < 10):
                roboMove.congrats()
                break
            if(keyboard_listener() == 1):
                break



