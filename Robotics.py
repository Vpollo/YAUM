import rospy, time
from geometry_msgs.msg import Twist
from CVV import cv_detection
from ultra import Ultra

forward_speed = 1600
backward_speed = 1440
stop_time = 0.1

class Robot_move:

    def __init__(self):
        # are there any?
        self.cvv = cv_detection()
        # link ultra sensor's trig to 13 and echo to 18
        self.ultrasonic = Ultra(13, 18)
        self.step = 1
        self.step_stop = 1

    def spin_and_detect(self, obj):
        # set up to spin
        backward_time = 1
        forward_time = 1
        pub = rospy.Publisher('car/cmd_vel', Twist, queue_size=10)
        rospy.init_node('publisher')
        rate = rospy.Rate(10) # 10hz

        # while loop to continuously turn and detect obj
        while not rospy.is_shutdown():
            msg = Twist()
            # right forward
            msg.angular.z = 66
            pub.publish(msg)       
            time.sleep(self.step)
            msg.linear.x = 1600
            pub.publish(msg)
            time.sleep(self.step)
            msg.linear.x = 1500
            msg.angular.z = 90
            pub.publish(msg)
            time.sleep(self.step_stop)
            if(self.cvv.detect_obj(obj)): break

            # left backward
            msg.angular.z = 114
            pub.publish(msg)
            time.sleep(self.step)
            msg.linear.x = 1460
            pub.publish(msg)
            time.sleep(0.1)
            msg.linear.x = 1500
            pub.publish(msg)
            time.sleep(0.1)
            msg.linear.x = 1460
            pub.publish(msg)
            time.sleep(1)
            if(self.cvv.detect_obj(obj)): break
            
            msg.linear.x = 1500
            msg.angular.z = 90
            pub.publish(msg)
            time.sleep(1)

    def turn_amount():
        dis_to_center = cvv.dis_to_center()
        # corelation between dis and turn should not be linear,
        # funcion fix later
        return dis_to_center


    # func to use cv to direct the robot to obj
    def to_target(self, obj):
        threshold = 10
        self.ultrasonic.setup()
        while(self.ultrasonic.distance_to_spitball>threshold):
            msg = Twist()
            msg.angular.z = turn_amount
            pub.publish(msg)

    #func to stop the robot
    def stop():
        msg = Twist()
        msg.linear.x = 1460
        pub.publish(msg)
        time.sleep(0.1)
        msg.linear.x = 1500
        pub.publish(msg)
        time.sleep(0.1)
        msg.linear.x = 1460
        pub.publish(msg)
        time.sleep(0.1)
        msg.linear.x = 1500
        pub.publish(msg)

    # func to congrats the owner if the throw hits
    #def congrats():
        # put congrats moves here
        # can include:[amrs movement, sound]
        



            
