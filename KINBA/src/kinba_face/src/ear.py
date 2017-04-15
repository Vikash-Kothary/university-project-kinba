#!/usr/bin/env python3
# ear.py

import rospy
from std_msgs.msg import String
from speech_to_text import speech_to_text


def publish(speechText):
    pub = rospy.Publisher('speech_to_text', String, queue_size=10)
    pub.publish(speechText)
    rospy.loginfo("Input: %s" % speechText)


def running():
    return not rospy.is_shutdown()

if __name__ == '__main__':
    rospy.init_node('ear', anonymous=True)
    speech_to_text()
    rospy.spin()
