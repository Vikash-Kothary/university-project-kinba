#!/usr/bin/env python3
# speech_to_text.py -

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


def running():
    return False


def publish(text):
    print(text)

if __name__ == '__main__':
    speech_to_text()
