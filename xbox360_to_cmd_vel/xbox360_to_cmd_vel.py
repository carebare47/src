#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    twist = Twist()
    # vertical left stick axis = linear rate
    twist.linear.x = data.axes[1]
    # horizontal left stick axis = turn rate
    twist.angular.z = data.axes[0]
    pub.publish(twist)

# Intializes everything
def start():
    rospy.init_node('Joy2cmdVel')
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('cmd_vel', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback, queue_size=1)
    # starts the node
    #rospy.init_node('Joy2cmdVel')
    rospy.spin()

if __name__ == '__main__':
    start()
