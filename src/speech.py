#! python3
# speech.py -

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function


def initProgramAB():
    kinba = Runtime.createAndStart("kinba", "ProgramAB")
    kinba.startSession()

    # create a Speech service
    mouth = Runtime.createAndStart("mouth", "Speech")
    # create a route which sends published Responses to the
    # mouth.speak(String) method
    kinba.addTextListener(mouth)

    print(kinba.getResponse("How are you?"))
    
if __name__ == '__main__':
    pass
