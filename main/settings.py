#! python3
# settings.py -

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function

#############################################
# Personality settings

male = False
lang = "EN"

#############################################
# Hardware specific settings

# Ports
#leftPort = ""
#rightPort = ""
#headPort = leftPort

#############################################
# Software speciic settings

# Artifical Intelligence Markup Language (AIML)
aimlPath = "../MyRobotLab/ProgramAB"
aimlBotName = "kinbaChatbot"
aimlUserName = "Vikash Kothary"
if male:
    botVoice = "Ryan"

# MarySpeech
# Default female for MarySpeech
voiceType = "cmu-slt-hsmm" 
if male:
	# Male US voice
    voiceType = "cmu-bdl-hsmm"

#############################################
# API keys

OPENWEATHERMAP_KEY = "7c256dfe06b95f67bc5cf3686cef1c5a"

if __name__ == '__main__':
    pass
