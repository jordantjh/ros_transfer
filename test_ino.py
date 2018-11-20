#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('command_card_t', String, queue_size=10)  # command_card_t is the topic name
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    counter = 0
    color_detected = "green"
    while counter < 20:
        rospy.loginfo(color_detected)
        pub.publish(color_detected)
        rate.sleep()
        counter += 1

    counter = 0
    color_detected = "yellow"
    while counter < 20:
        rospy.loginfo(color_detected)
        pub.publish(color_detected)
        rate.sleep()
        counter += 1

    counter = 0
    color_detected = "red"
    while counter < 20:
        rospy.loginfo(color_detected)
        pub.publish(color_detected)
        rate.sleep()
        counter += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass