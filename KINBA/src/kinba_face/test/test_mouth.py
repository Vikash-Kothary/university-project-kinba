#!/usr/bin/env python3
# test_mouth.py - Tests mouth

import sys
import unittest
import rospy
from std_msgs.msg import String


# class TestMouth(unittest.TestCase):

#     def test_input(self):
#         pub = rospy.Publisher('text_to_speech', String, queue_size=10)
#         pub.publish('Hello World')
#         pub.publish('My name is Kinba')


# class TestTextToSpeech(unittest.TestCase):

#     def test_hello_world(self):
#         expected = ""
#         actual = ""
#         self.assertEquals(expected, actual)


# def main():
#     import rostest
#     package_name = "test_mouth"
#     test_name = "test_mouth"
#     test_case_class = TestMouth
#     rostest.rosrun(package_name, test_name, test_case_class)


if __name__ == '__main__':
    try:
        pub = rospy.Publisher('text_to_speech', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        # rate = rospy.Rate(100)  # 10hz
        # while not rospy.is_shutdown():
        if True:
            hello_str = "hello world"
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
        #    rate.sleep()
    except rospy.ROSInterruptException:
        pass
