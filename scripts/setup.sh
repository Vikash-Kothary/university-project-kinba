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
DIRECTORY="myrobotlab"
FILENAME="myrobotlab.jar"
mkdir $DIRECTORY
cd $DIRECTORY
if [ ! -f $FILENAME ]; then
    # Download latest MyRobotLab file
    wget "https://github.com/MyRobotLab/myrobotlab/releases/download/$LATEST_VERSION/$FILENAME"

    # Install all required MyRobotLab services
    java -jar $FILENAME -install ProgramAB MarySpeech WebkitSpeechRecognition OpenCV

    # Install male MarySpeech voice
    wget "https://github.com/MyRobotLab/pyrobotlab/blob/ff6e2cef4d0642e47ee15e353ef934ac6701e713/home/hairygael/voice-cmu-bdl-5.2.jar"
    mv "voice-cmu-bdl-5.2.jar" "libraries/jar/."

    # Move code to correct folders
    mkdir "ProgramAB/bots/kinbaChatbot/aiml/"
    cp "../aiml/" "ProgramAB/bots/kinbaChatbot/aiml/"
    cp -r "../main/" "pythonModules/"

    # Set project to run on boot
    # run.sh
fi
cd ..

# Install python requirements
pip install pyowm

# Move python scripts into folder

# Run MyRobotLab
sh "scripts/run.sh"
#java -jar "$DIRECTORY/$FILENAME"
