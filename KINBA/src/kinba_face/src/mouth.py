#!/usr/bin/env python3
# mouth.py

import rospy
from std_msgs.msg import String
import pyttsx
import os
import subprocess


def text_to_speech(text):
    speech_pyttsx(text)


def execute_unix(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output


def speech_espeak(text):
    print('Espeak: %s' % text)
    execute_unix("espeak '%s'" % text)


def speech_pyttsx(text):
    print('Pyttsx: %s' % text)
    engine = pyttsx.init()
    engine.say(text)

def speech(data):
    print("Kinba: %s" % data.data)
    text_to_speech(data.data)


def main():
    rospy.init_node('mouth', anonymous=True)
    rospy.Subscriber('speech', String, speech)
    rospy.spin()

if __name__ == '__main__':
    main()
