#!/usr/bin/env python3
# ear.py

import rospy
from std_msgs.msg import String
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as speech:
        r.adjust_for_ambient_noise(speech)
        while running():
            print("==> Say something!")
            audio = r.listen(speech)
            print("==> Recognising")
            try:
                text = r.recognize_google(audio)
                publish(text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(e))


def publish(speechText):
    pub = rospy.Publisher('speech', String, queue_size=10)
    pub.publish(speechText)
    rospy.loginfo("User: %s" % speechText)


def running():
    return not rospy.is_shutdown()


def main():
    rospy.init_node('ear', anonymous=True)
    speech_to_text()
    rospy.spin()

# debugging mode allows users to enter text using the keyboard
def debug():
    rospy.init_node('ear_debug', anonymous=True)
    while running():
        text = input('User: ')
        publish(text)
    rospy.spin()

if __name__ == '__main__':
    debug()
