#!/usr/bin/env python3
# text_to_speech.py -

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
    engine.runAndWait()


if __name__ == '__main__':
    text_to_speech('Hello World')
    text_to_speech('My name is Kinba')
