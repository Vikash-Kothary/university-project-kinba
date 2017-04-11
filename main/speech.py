#! python3
# speech.py -

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function
#from settings import aimlPath, aimlBotName, aimlUserName, voiceType, lang


male = False
lang = "EN"

# Artifical Intelligence Markup Language (AIML)
aimlPath = "../aiml"
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


def main():
    # create ProgramAB chat bot
    chatbot = Runtime.createAndStart("kinbaChatbot", "ProgramAB")
    chatbot.startSession(aimlUserName, aimlBotName)
    chatbot.setPath(aimlPath)

    html_filter = Runtime.createAndStart('htmlfilter', "HtmlFilter")

    # chatbot outputs are sent to the html filter
    chatbot.addTextListener(html_filter)
    # html filter outputs are sent to the mouth
    if mouth:
        html_filter.addTextListener(mouth)

    return chatbot

    # Speech Synthesis
    # mouth = Runtime.createAndStart("mouth", "Speech")
    mouth = Runtime.createAndStart("mouth", "MarySpeech")
    # mouth = Runtime.createAndStart("mouth", "AcapelaSpeech")
    # mouth.setVoice(voiceType)
    # mouth.setLanguage(lang)

    input_text = "How are you?"
    output_text = chatbot.getResponse(input_text)
    print(output_text)

    # Webkit Speech Recognition
    ear = Runtime.createAndStart("ears", "WebkitSpeechRecognition")
    ear.addListener("publishText", python.name, "heard")
    ear.addMouth(mouth)

    WebkitSpeechRecognitionFix = Runtime.start(
        "WebkitSpeechRecognitionFix", "Clock")
    WebkitSpeechRecognitionFix.setInterval(1000)
    WebkitSpeechRecognitionFix.startClock()
    # MRL Routing webkitspeechrecognition/ear -> program ab -> htmlfilter ->
    # mouth
    ear.addTextListener(inmoovWebKit)
    inmoovWebKit.addTextListener(htmlfilter)
    htmlfilter.addTextListener(mouth)

    python.subscribe(ear.getName(), "publishText")

if __name__ == '__main__':
    main()
