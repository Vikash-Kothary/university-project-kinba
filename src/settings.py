#! python3
# settings.py -

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function


#############################################
# Hardware specific settings

# Ports
leftPort = ""
rightPort = ""
headPort = leftPort

# Artifical Intelligence Markup Language (AIML)
aimlPath = ""
aimlBotName = "kinbaWebKit"
aimlUserName = "Vikash Kothary"
if male:
    botVoice = "Ryan"

#############################################

male = False
lang = "EN"
if male:
    Voice = "cmu-bdl-hsmm"
    # Male US voice.You need to add the necessary file.jar to
    # myrobotlab.1.0.XXXX/library/jar
else:
    Voice = "cmu-slt-hsmm"  # Default female for MarySpeech
voiceType = Voice

#############################################
# API keys

microsoft_client_id = "your_id"
microsoft_client_secret = "yoursecret_key"


if __name__ == '__main__':
    pass
