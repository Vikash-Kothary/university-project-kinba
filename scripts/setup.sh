#!/bin/bash
# setup.sh - Setup project

# Install Java, if not already installed
sudo apt-get -qq update
sudo apt-get -qq upgrade
if [ -n `which java` ]; then
    sudo apt-get install -y default-jre
    sudo apt-get install -y default-jdk
fi
if [ -n `which virtualenv` ]; then
    sudo apt-get install virtualenv
fi

# Setup virtual environment
virtualenv venv
. venv/bin/activate

# Install MyRobotLab
LATEST_VERSION="1.0.1758"
DIRECTORY="MyRobotLab"
FILENAME="myrobotlab.jar"
mkdir $DIRECTORY
cd $DIRECTORY
if [ ! -f $FILENAME ]; then
	# Download latest MyRobotLab file
    wget "https://github.com/MyRobotLab/myrobotlab/releases/download/$LATEST_VERSION/$FILENAME"

    # Install all required MyRobotLab services
    java -jar $FILENAME -install ProgramAB MarySpeech WebkitSpeechRecognition OpenCV

    # Set project to run on boot
    # boot.sh
fi
cd ..

# Move python scripts into folder

# Run MyRobotLab
#java -jar "$DIRECTORY/$FILENAME"
