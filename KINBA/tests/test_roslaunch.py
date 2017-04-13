#!/usr/bin/env python
# test_speech_recognition.py - Tests roslaunch

import sys
import unittest


class TestAudioInput(unittest.TestCase):

    def test_input(self):
        expected = ""
        actual = ""
        self.assertEquals(expected, actual)


class TestRecognition(unittest.TestCase):

    def test_hello_world(self):
        expected = ""
        actual = ""
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    import rostest.
    package_name = "test_speech_recognition"
    test_name = "test_audio_input"
    test_case_class = TestAudioInput
    rostest.rosrun(package_name, test_name, test_case_class)
