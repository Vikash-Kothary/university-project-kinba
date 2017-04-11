#!/usr/bin/env python
# vision.py - 

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function


# start services
# Runtime.start(name, service) or runtime.createAndStart(name, service)
python = Runtime.start("python","Python")
opencv = Runtime.start("opencv","OpenCV")

# Add python as a listener to OpenCV data
# Call python.onOpenCVData whenever opencv.publishOpenCVData is invoked

def onOpenCVData(data):