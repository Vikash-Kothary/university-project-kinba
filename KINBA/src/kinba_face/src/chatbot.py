#!/usr/bin/env python3
# chatbot.py -

import os.path
import sys
import json
#import rospy
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
CLIENT_ACCESS_TOKEN = '4a2eedad86774b08b5b63568e8d5a9fa'


def publish(speechText):
    pub = rospy.Publisher('speech', String, queue_size=10)
    pub.publish(speechText)
    rospy.loginfo("Kinba: %s" % speechText)

def main():
    if True:#while(True):
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        request = ai.text_request()

        request.query = 'What is the weather?'

        response = request.getresponse()
        responsestr = response.read().decode('utf-8')
        response_obj = json.loads(responsestr)

        output = response_obj["result"]["fulfillment"]["speech"]
        publish(str(output))
        #publish(output)

if __name__ == '__main__':
    main()