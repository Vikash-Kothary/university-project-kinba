#! python3
# main.py -

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function
import speech

# rnu as chatbot only
startVision = False

# create ear and mouth
ear = Runtime.createAndStart("ear", "Sphinx")
mouth = Runtime.createAndStart("mouth", "Speech")

# start listening for the words we are interested in
ear.startListening(
    "hello | forward | back | stop | go |turn left | turn right | spin | power off")


# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", python.getName(), "heard")

# this method is invoked when something is
# recognized by the ear - in this case we
# have the mouth "talk back" the word it recognized


def heard(data):
    # data = msg_ear_recognized.data[0]
    mouth.speak("you said " + data)
    print "heard ", data
    if (data == "forward"):
        print "robot goes forward"
    elif (data == "hello"):
        print "robot says hello"
   # ... etc

# prevent infinite loop - this will suppress the
# recognition when speaking - default behavior
# when attaching an ear to a mouth :)
ear.attach("mouth")

if __name__ == '__main__':
    pass
